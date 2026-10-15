// Repeatable native Excalidraw conversion + actual React editor acceptance, local-only.
// Run build-extra-01-05.py first. Dependencies are read from the existing scratch install.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../..');
const cache=path.join(process.env.HOME,'.hermes/profiles/curriculum-dev/cache/scratch');
const scratch=path.join(cache,'ds-diagrams-extra-01-05');
const deps=path.join(cache,'oop-excalidraw');
const require=createRequire(path.join(deps,'package.json'));
const {chromium}=require('playwright');
const {createServer}=await import(require.resolve('vite'));
await fs.mkdir(path.join(scratch,'evidence'),{recursive:true});
try{await fs.symlink(path.join(deps,'node_modules'),path.join(scratch,'node_modules'));}catch(e){if(e.code!=='EEXIST')throw e;}
await fs.writeFile(path.join(scratch,'index.html'),'<html><body style="margin:0"><div id="root" style="width:1240px;height:850px"></div><script type="module" src="/harness.jsx"></script></body></html>');
await fs.writeFile(path.join(scratch,'harness.jsx'),`import React from 'react'; import {createRoot} from 'react-dom/client'; import * as E from '@excalidraw/excalidraw'; import '@excalidraw/excalidraw/index.css'; window.E=E; createRoot(document.getElementById('root')).render(<E.Excalidraw excalidrawAPI={api=>window.api=api}/>);`);
const server=await createServer({root:scratch,configFile:false,server:{host:'127.0.0.1',port:0,fs:{allow:[scratch,deps]}},logLevel:'error'});
await server.listen();
const browser=await chromium.launch({headless:true});
const report=[];
try{
const page=await browser.newPage({viewport:{width:1240,height:850}});
const renderPage=await browser.newPage({viewport:{width:1240,height:1520},deviceScaleFactor:1});
const errors=[];page.on('pageerror',e=>errors.push(String(e)));
await page.route('**/*',r=>new URL(r.request().url()).hostname==='127.0.0.1'?r.continue():r.abort());
await page.goto(server.resolvedUrls.local[0]);await page.waitForFunction(()=>window.api&&window.E);
const placements=JSON.parse(await fs.readFile(path.join(here,'placements-extra-01-05.json'),'utf8'));
if(placements.length!==32)throw Error('Expected 32 placements');
const sources=[],renders=[];
for(const p of placements){
 const source=await fs.readFile(path.join(here,p.file),'utf8');
 const result=await page.evaluate(async source=>{
  const E=window.E,svg=new DOMParser().parseFromString(source,'image/svg+xml').documentElement;
  const list=[],cards=[];let serial=0;
  const n=(node,key,def=0)=>Number(node.getAttribute(key)??def);
  const base=(node,type)=>({id:'e'+(++serial),type,x:n(node,'x'),y:n(node,'y'),strokeColor:node.getAttribute('stroke')||'transparent',backgroundColor:node.getAttribute('fill')||'transparent',fillStyle:'solid',strokeWidth:n(node,'stroke-width',1),roughness:0,opacity:100,angle:0,groupIds:[],locked:false,roundness:null});
  function walk(node,group=null){
   const tag=node.tagName;
   if(['defs','title','desc'].includes(tag))return;
   if(tag==='g'){
    const id='group-'+(++serial),members=[];
    for(const child of node.children){const e=walk(child,id);if(e)members.push(e);}
    const rect=members.find(e=>e.type==='rectangle'),texts=members.filter(e=>e.type==='text');
    if(rect){cards.push(rect);if(texts.length===1){texts[0].containerId=rect.id;texts[0].verticalAlign='middle';rect.boundElements=[{id:texts[0].id,type:'text'}];}}
    return;
   }
   let el;
   if(tag==='rect'){
    el={...base(node,'rectangle'),width:n(node,'width'),height:n(node,'height'),roundness:n(node,'rx')?{type:3}:null};if(!group)el.locked=true;
   }else if(tag==='text'){
    const size=n(node,'font-size',20),text=node.textContent;
    const ctx=document.createElement('canvas').getContext('2d');ctx.font=size+'px Arial';const width=ctx.measureText(text).width;
    el={...base(node,'text'),x:n(node,'x')-width/2,y:n(node,'y')-size,width,height:size*1.25,text,originalText:text,fontSize:size,fontFamily:2,lineHeight:1.25,textAlign:'center',verticalAlign:'top',containerId:null,autoResize:true,strokeColor:node.getAttribute('fill'),backgroundColor:'transparent'};
   }else if(tag==='path'&&node.hasAttribute('data-connector')){
    const coords=node.getAttribute('d').match(/-?\d+(?:\.\d+)?/g).map(Number),points=[];
    for(let i=0;i<coords.length;i+=2)points.push([coords[i]-coords[0],coords[i+1]-coords[1]]);
    el={...base(node,'arrow'),x:coords[0],y:coords[1],width:Math.max(...points.map(p=>p[0]))-Math.min(...points.map(p=>p[0])),height:Math.max(...points.map(p=>p[1]))-Math.min(...points.map(p=>p[1])),points,startArrowhead:null,endArrowhead:'triangle',startBinding:null,endBinding:null,elbowed:false};
   }
   if(el){if(group)el.groupIds=[group];list.push(el);return el;}
  }
  for(const node of svg.children)walk(node);
  for(const arrow of list.filter(e=>e.type==='arrow')){
   for(const [key,pt] of [['startBinding',arrow.points[0]],['endBinding',arrow.points.at(-1)]]){
    const x=arrow.x+pt[0],y=arrow.y+pt[1];
    const card=cards.find(c=>x>=c.x-.1&&x<=c.x+c.width+.1&&y>=c.y-.1&&y<=c.y+c.height+.1&&(Math.abs(x-c.x)<.1||Math.abs(x-c.x-c.width)<.1||Math.abs(y-c.y)<.1||Math.abs(y-c.y-c.height)<.1));
    if(card){arrow[key]={elementId:card.id,focus:0,gap:0,fixedPoint:[(x-card.x)/card.width,(y-card.y)/card.height]};card.boundElements??=[];card.boundElements.push({id:arrow.id,type:'arrow'});}
   }
  }
  let elements=E.convertToExcalidrawElements(list,{regenerateIds:false});
  elements=elements.map(e=>{const src=list.find(s=>s.id===e.id);return {...e,...(e.type==='text'?{x:src.x+src.width/2-e.width/2,y:src.y}:{}),groupIds:src.groupIds,boundElements:src.boundElements||null,...(e.type==='arrow'?{startBinding:src.startBinding,endBinding:src.endBinding}:{}),updated:1,seed:1000+list.indexOf(src),versionNonce:1000+list.indexOf(src)};});
  const texts=[...svg.querySelectorAll('text')].map(e=>e.textContent);
  if(JSON.stringify(elements.filter(e=>e.type==='text').map(e=>e.originalText))!==JSON.stringify(texts))throw Error('Source text mismatch');
  if(elements.some(e=>!['text','rectangle','arrow'].includes(e.type)))throw Error('Non-native element');
  const overflow=elements.filter(e=>e.type==='text'&&(e.x<0||e.x+e.width>1240||e.y<0||e.y+e.height>760)).map(e=>e.text);
  if(overflow.length)throw Error('Off-canvas text: '+JSON.stringify(overflow));
  const appState={viewBackgroundColor:'#ffffff',theme:'light',gridSize:null,exportBackground:true,exportWithDarkMode:false};
  const json=E.serializeAsJSON(elements,appState,{},'local');
  const imported=await E.loadFromBlob(new Blob([json],{type:'application/vnd.excalidraw+json'}),null,null);
  window.api.updateScene({elements:imported.elements,appState});window.api.scrollToContent(imported.elements,{fitToContent:true});
  await new Promise(r=>setTimeout(r,70));
  const loaded=window.api.getSceneElements();if(loaded.length!==elements.length)throw Error('Dropped elements');
  const render=await E.exportToSvg({elements:loaded,appState,files:{},exportPadding:0});
  const target=loaded.find(e=>e.type==='text'&&!e.containerId);
  const edited=loaded.map(e=>e.id===target.id?{...e,text:e.text+' [EDIT TEST]',originalText:e.originalText+' [EDIT TEST]',version:e.version+1}:e);
  window.api.updateScene({elements:edited});
  const editedSvg=await E.exportToSvg({elements:window.api.getSceneElements(),appState,files:{},exportPadding:0});
  if(!editedSvg.textContent.includes('[EDIT TEST]'))throw Error('Edit export failed');
  const editedJson=E.serializeAsJSON(window.api.getSceneElements(),appState,{},'local');
  const reloaded=await E.loadFromBlob(new Blob([editedJson]),null,null);
  if(!reloaded.elements.some(e=>e.text?.includes('[EDIT TEST]')))throw Error('Edited reimport failed');
  window.api.updateScene({elements:imported.elements,appState});
  return {json,render:render.outerHTML,editedSvg:editedSvg.outerHTML,stats:{elements:loaded.length,texts:loaded.filter(e=>e.type==='text').length,arrows:loaded.filter(e=>e.type==='arrow').length,rectangles:loaded.filter(e=>e.type==='rectangle').length,boundTexts:loaded.filter(e=>e.type==='text'&&e.containerId).length,boundArrowEnds:loaded.filter(e=>e.type==='arrow').reduce((n,e)=>n+!!e.startBinding+!!e.endBinding,0),sourceTextParity:true,import:true,mountedEditor:true,exportSvg:true,editedExport:true,editedReimport:true,noImages:true,offCanvasText:overflow}};
 },source);
 const bytes=result.json+'\n';await fs.writeFile(path.join(here,p.editable),bytes);await fs.writeFile(path.join(root,p.local_editable),bytes);
 if((await fs.readFile(path.join(root,p.local_editable),'utf8'))!==bytes)throw Error('Native copy mismatch');
 if((await fs.readFile(path.join(root,p.local_svg),'utf8'))!==source)throw Error('SVG copy mismatch');
 const stem=p.file.replace('.svg','');
 await fs.writeFile(path.join(scratch,'evidence',stem+'-export.svg'),result.render);
 await fs.writeFile(path.join(scratch,'evidence',stem+'-edited.svg'),result.editedSvg);
 await page.screenshot({path:path.join(scratch,'evidence',stem+'-editor.png')});
 sources.push(source);renders.push(result.render);report.push({file:p.file,...result.stats,byteIdentical:true});
 console.log('Verified '+report.length+'/32 '+p.file);
}
// Two large diagrams per contact sheet, separate canonical and native-export sheets.
for(const [kind,items] of [['source',sources],['native',renders]]){
 for(let i=0;i<items.length;i+=2){
  await renderPage.setContent('<html><body style="margin:0;background:white">'+items.slice(i,i+2).map(svg=>'<div style="width:1240px;height:760px">'+svg.replace(/<svg\b/,'<svg style="width:1240px;height:760px;display:block"')+'</div>').join('')+'</body></html>');
  await renderPage.screenshot({path:path.join(scratch,'evidence',kind+'-contact-'+String(i/2+1).padStart(2,'0')+'.png')});
 }
}
if(errors.length)throw Error(errors.join('\n'));
const version=JSON.parse(await fs.readFile(path.join(deps,'node_modules/@excalidraw/excalidraw/package.json'),'utf8')).version;
const audit=JSON.parse(await fs.readFile(path.join(here,'audit-extra-01-05.json'),'utf8'));
Object.assign(audit,{native_acceptance:{libraryVersion:version,browser:browser.version(),externalRequestsBlocked:true,figures:report.length,results:report},evidence:scratch+'/evidence',native_limitations:['Text is native editable Arial; SVG bold weight is not used.','Multi-line cards use grouped separate text elements; resizing may require manual text adjustment.','Connectors are native arrows with reciprocal endpoint bindings where endpoints meet node edges; bends may need manual adjustment.']});
await fs.writeFile(path.join(here,'audit-extra-01-05.json'),JSON.stringify(audit,null,2)+'\n');
console.log(JSON.stringify({verified:report.length,libraryVersion:version,evidence:scratch+'/evidence'}));
}finally{await browser.close();await server.close();}
