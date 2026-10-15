// Real-library SVG/native acceptance; reusable for this SVG grammar.
// Run after build-first-half.py. Evidence and dependencies stay in scratch.
// Override DIAGRAM_PLACEMENTS and DIAGRAM_AUDIT to reuse without editing group files.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../..');
const base=path.join(process.env.HOME,'.hermes/profiles/curriculum-dev/cache/scratch');
const deps=process.env.EXCALIDRAW_DEPENDENCIES||path.join(base,'oop-excalidraw');
const scratch=process.env.DIAGRAM_EVIDENCE_DIR||path.join(base,'data-structures-first-half');
const require=createRequire(path.join(deps,'package.json'));
const {chromium}=require('playwright');
const {createServer}=await import(require.resolve('vite'));
await fs.mkdir(path.join(scratch,'evidence'),{recursive:true});
try{await fs.symlink(path.join(deps,'node_modules'),path.join(scratch,'node_modules'),'dir')}catch(e){if(e.code!=='EEXIST')throw e}
await fs.writeFile(path.join(scratch,'index.html'),'<html><body style="margin:0"><div id="root" style="width:1000px;height:1000px"></div><script type="module" src="/harness.jsx"></script></body></html>');
await fs.writeFile(path.join(scratch,'harness.jsx'),`import React from 'react';import {createRoot} from 'react-dom/client';import * as E from '@excalidraw/excalidraw';import '@excalidraw/excalidraw/index.css';window.E=E;createRoot(document.getElementById('root')).render(<E.Excalidraw excalidrawAPI={api=>window.api=api}/>);`);
const server=await createServer({root:scratch,configFile:false,server:{host:'127.0.0.1',port:0,fs:{allow:[scratch,deps]}},logLevel:'error'});await server.listen();
const browser=await chromium.launch({headless:true});
const evidence=path.join(scratch,'evidence');
try{
 const page=await browser.newPage({viewport:{width:1050,height:1050}});
 const svgPage=await browser.newPage({viewport:{width:500,height:700},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.route('**/*',route=>new URL(route.request().url()).hostname==='127.0.0.1'?route.continue():route.abort());
 await svgPage.route('**/*',route=>route.abort());
 await page.goto(server.resolvedUrls.local[0]);await page.waitForFunction(()=>window.api&&window.E);
 const placements=JSON.parse(await fs.readFile(process.env.DIAGRAM_PLACEMENTS||path.join(here,'placements-first-half.json'),'utf8'));
 const report=[];
 for(const placement of placements){
  const source=await fs.readFile(path.join(root,placement.canonical_svg),'utf8');
  const name=placement.editable,stem=placement.file.replace('.svg','');
  await svgPage.setContent('<html><body style="margin:0">'+source+'</body></html>');
  await svgPage.evaluate(()=>document.fonts.ready);
  const geometry=await svgPage.evaluate(()=>{
   const svg=document.querySelector('svg'),W=svg.viewBox.baseVal.width,H=svg.viewBox.baseVal.height;
   const texts=[...svg.querySelectorAll('text')].map(e=>({text:e.textContent,b:e.getBBox()}));
   const overlaps=[],outOfBounds=[],arrowCrossings=[];
   const intersect=(a,b)=>Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1;
   texts.forEach((a,i)=>{if(a.b.x<0||a.b.y<0||a.b.x+a.b.width>W||a.b.y+a.b.height>H)outOfBounds.push(a.text);texts.slice(i+1).forEach(b=>{if(intersect(a.b,b.b))overlaps.push([a.text,b.text])})});
   const shapes=[...svg.querySelectorAll('g rect')].map(e=>({label:e.parentNode.textContent,b:e.getBBox()}));
   // Sample each segment at subpixel spacing, testing strict interior so edge bindings pass.
   for(const a of svg.querySelectorAll('[data-connector]')){
    const nums=a.getAttribute('d').match(/-?\d+(?:\.\d+)?/g).map(Number),points=[];
    for(let i=0;i<nums.length;i+=2)points.push([nums[i],nums[i+1]]);
    for(let i=1;i<points.length;i++){
     const [x,y]=points[i-1],[xx,yy]=points[i],steps=Math.ceil(Math.hypot(xx-x,yy-y)*2);
     for(const obj of [...texts,...shapes]){
      const b=obj.b;let hit=false;
      for(let k=0;k<=steps;k++){const px=x+(xx-x)*k/steps,py=y+(yy-y)*k/steps;if(px>b.x+.5&&px<b.x+b.width-.5&&py>b.y+.5&&py<b.y+b.height-.5){hit=true;break}}
      if(hit)arrowCrossings.push({path:a.getAttribute('d'),target:obj.text||obj.label});
     }
    }
   }
   return {width:W,height:H,textCount:texts.length,outOfBounds,textOverlaps:overlaps,arrowCrossings,accessibleTitle:!!svg.querySelector('title')?.textContent,accessibleDescription:!!svg.querySelector('desc')?.textContent};
  });
  await svgPage.locator('svg').screenshot({path:path.join(evidence,stem+'-original.png')});
  const result=await page.evaluate(async({source,name})=>{
   const E=window.E,svg=new DOMParser().parseFromString(source,'image/svg+xml').documentElement;
   const list=[],cards=[];let serial=0;
   const n=(node,key,def=0)=>Number(node.getAttribute(key)??def);
   const base=(node,type)=>({id:'e'+(++serial),type,x:n(node,'x'),y:n(node,'y'),strokeColor:node.getAttribute('stroke')||'transparent',backgroundColor:node.getAttribute('fill')||'transparent',fillStyle:'solid',strokeWidth:n(node,'stroke-width',1),roughness:0,opacity:100,angle:0,groupIds:[],locked:false,roundness:null});
   function walk(node,group=null){
    const tag=node.tagName;if(['defs','title','desc'].includes(tag))return;
    if(tag==='g'){
     const groupId='group-'+(++serial),members=[];
     for(const c of node.children){const e=walk(c,groupId);if(e)members.push(e)}
     const rect=members.find(e=>e.type==='rectangle'),texts=members.filter(e=>e.type==='text');if(rect)cards.push(rect);
     if(rect&&texts.length===1){texts[0].containerId=rect.id;texts[0].verticalAlign='middle';rect.boundElements=[{id:texts[0].id,type:'text'}]}
     return;
    }
    let el;
    if(tag==='rect'){el={...base(node,'rectangle'),width:n(node,'width'),height:n(node,'height'),roundness:n(node,'rx')?{type:3}:null};if(!group)el.locked=true}
    else if(tag==='text'){
     const size=n(node,'font-size',16),text=node.textContent,ctx=document.createElement('canvas').getContext('2d');ctx.font=size+'px Arial';
     const width=ctx.measureText(text).width,anchor=node.getAttribute('text-anchor')||'start';
     el={...base(node,'text'),x:n(node,'x')-(anchor==='middle'?width/2:anchor==='end'?width:0),y:n(node,'y')-size,width,height:size*1.25,text,originalText:text,fontSize:size,fontFamily:2,lineHeight:1.25,textAlign:anchor==='middle'?'center':'left',verticalAlign:'top',containerId:null,autoResize:true,strokeColor:node.getAttribute('fill'),backgroundColor:'transparent'};
    }else if(tag==='path'&&node.hasAttribute('data-connector')){
     const coords=node.getAttribute('d').match(/-?\d+(?:\.\d+)?/g).map(Number),points=[];
     for(let i=0;i<coords.length;i+=2)points.push([coords[i]-coords[0],coords[i+1]-coords[1]]);
     el={...base(node,'arrow'),x:coords[0],y:coords[1],width:Math.max(...points.map(p=>p[0]))-Math.min(...points.map(p=>p[0])),height:Math.max(...points.map(p=>p[1]))-Math.min(...points.map(p=>p[1])),points,startArrowhead:null,endArrowhead:'triangle',startBinding:null,endBinding:null,elbowed:false};
    }
    if(el){if(group)el.groupIds=[group];list.push(el);return el}
   }
   for(const node of svg.children)walk(node);
   for(const arrow of list.filter(e=>e.type==='arrow')){
    for(const [key,p] of [['startBinding',arrow.points[0]],['endBinding',arrow.points.at(-1)]]){
     const x=arrow.x+p[0],y=arrow.y+p[1];
     const card=cards.find(c=>x>=c.x-.1&&x<=c.x+c.width+.1&&y>=c.y-.1&&y<=c.y+c.height+.1&&(Math.abs(x-c.x)<.1||Math.abs(x-c.x-c.width)<.1||Math.abs(y-c.y)<.1||Math.abs(y-c.y-c.height)<.1));
     if(card){arrow[key]={elementId:card.id,focus:0,gap:0,fixedPoint:[(x-card.x)/card.width,(y-card.y)/card.height]};card.boundElements??=[];card.boundElements.push({id:arrow.id,type:'arrow'})}
    }
   }
   let elements=E.convertToExcalidrawElements(list,{regenerateIds:false});
   elements=elements.map(e=>{const s=list.find(s=>s.id===e.id);return {...e,...(e.type==='text'?{x:s.x+(s.width-e.width)/2,y:s.y}:{}),groupIds:s.groupIds,boundElements:s.boundElements||null,...(e.type==='arrow'?{startBinding:s.startBinding,endBinding:s.endBinding}:{}),updated:1,seed:1000+list.indexOf(s),versionNonce:1000+list.indexOf(s)}});
   const texts=[...svg.querySelectorAll('text')].map(e=>e.textContent);
   if(JSON.stringify(elements.filter(e=>e.type==='text').map(e=>e.originalText))!==JSON.stringify(texts))throw Error('Text mismatch');
   if(elements.some(e=>!['text','rectangle','arrow'].includes(e.type)))throw Error('Non-native element');
   const appState={viewBackgroundColor:'#ffffff',theme:'light',gridSize:null,exportBackground:true,exportWithDarkMode:false};
   const json=E.serializeAsJSON(elements,appState,{},'local');
   const imported=await E.loadFromBlob(new Blob([json],{type:'application/vnd.excalidraw+json'}),null,null);
   window.api.updateScene({elements:imported.elements,appState});window.api.scrollToContent(imported.elements,{fitToContent:true});await new Promise(r=>setTimeout(r,120));
   const loaded=window.api.getSceneElements();if(loaded.length!==elements.length)throw Error('Dropped elements');
   const rendered=await E.exportToSvg({elements:loaded,appState,files:{},exportPadding:0});
   const text=loaded.find(e=>e.type==='text'&&!e.containerId);
   const edited=loaded.map(e=>e.id===text.id?{...e,text:e.text+' [EDIT TEST]',originalText:e.originalText+' [EDIT TEST]',version:e.version+1}:e);
   window.api.updateScene({elements:edited});
   const editExport=await E.exportToSvg({elements:window.api.getSceneElements(),appState,files:{},exportPadding:0});
   if(!editExport.textContent.includes('[EDIT TEST]'))throw Error('Edit not exported');
   const editJson=E.serializeAsJSON(window.api.getSceneElements(),appState,{},'local');
   const reloaded=await E.loadFromBlob(new Blob([editJson]),null,null);
   if(!reloaded.elements.some(e=>e.text?.includes('[EDIT TEST]')))throw Error('Edit not reimported');
   window.api.updateScene({elements:reloaded.elements,appState});
   if(!window.api.getSceneElements().some(e=>e.text?.includes('[EDIT TEST]')))throw Error('Reimport not mounted');
   window.api.updateScene({elements:imported.elements,appState});
   const count=t=>loaded.filter(e=>e.type===t).length;
   const nativeGeometry={outOfBounds:[],textOverlaps:[],arrowCrossings:[]};
   const W=Number(svg.getAttribute('width')),H=Number(svg.getAttribute('height'));
   const ts=loaded.filter(e=>e.type==='text'),rs=loaded.filter(e=>e.type==='rectangle'&&!e.locked);
   for(let i=0;i<ts.length;i++){
    const a=ts[i];if(a.x<0||a.y<0||a.x+a.width>W+.5||a.y+a.height>H+.5)nativeGeometry.outOfBounds.push(a.text);
    for(const b of ts.slice(i+1))if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1)nativeGeometry.textOverlaps.push([a.text,b.text]);
   }
   for(const a of loaded.filter(e=>e.type==='arrow'))for(let i=1;i<a.points.length;i++){
    const [dx,dy]=a.points[i-1],[ex,ey]=a.points[i],steps=Math.ceil(Math.hypot(ex-dx,ey-dy)*2);
    for(const b of [...ts,...rs]){
     let hit=false;for(let k=0;k<=steps;k++){const x=a.x+dx+(ex-dx)*k/steps,y=a.y+dy+(ey-dy)*k/steps;if(x>b.x+.5&&x<b.x+b.width-.5&&y>b.y+.5&&y<b.y+b.height-.5){hit=true;break}}
     if(hit)nativeGeometry.arrowCrossings.push({arrow:a.id,target:b.text||b.id});
    }
   }
   return {json,render:rendered.outerHTML,editedRender:editExport.outerHTML,editedJson:editJson,stats:{nativeGeometry,nativeElements:loaded.length,text:count('text'),rectangles:count('rectangle'),arrows:count('arrow'),images:count('image'),textParity:true,import:true,editorMounted:true,export:true,textEditExport:true,editedFileReimport:true,editedFileRemounted:true,boundArrowEnds:loaded.filter(e=>e.type==='arrow').reduce((n,e)=>n+!!e.startBinding+!!e.endBinding,0)}};
  },{source,name});
  await fs.writeFile(path.join(root,placement.canonical_editable),result.json+'\n');
  await fs.writeFile(path.join(root,placement.local_editable),result.json+'\n');
  const equal=async(a,b)=>(await fs.readFile(path.join(root,a))).equals(await fs.readFile(path.join(root,b)));
  const identical={svg:await equal(placement.canonical_svg,placement.local_svg),excalidraw:await equal(placement.canonical_editable,placement.local_editable)};
  await fs.writeFile(path.join(evidence,stem+'-export.svg'),result.render);await fs.writeFile(path.join(evidence,stem+'-edited.svg'),result.editedRender);await fs.writeFile(path.join(evidence,stem+'-edited.excalidraw'),result.editedJson);
  await page.screenshot({path:path.join(evidence,stem+'-editor.png')});
  await svgPage.setContent('<html><body style="margin:0">'+result.render+'</body></html>');
  await svgPage.locator('svg').screenshot({path:path.join(evidence,stem+'-export.png')});
  report.push({file:placement.file,...result.stats,geometry,byteIdentical:identical,evidence:{original:stem+'-original.png',editor:stem+'-editor.png',export:stem+'-export.svg',editedExport:stem+'-edited.svg',editedReimport:stem+'-edited.excalidraw'}});
 }
 const version=JSON.parse(await fs.readFile(path.join(deps,'node_modules/@excalidraw/excalidraw/package.json'),'utf8')).version;
 const failed=report.filter(r=>r.geometry.outOfBounds.length||r.geometry.textOverlaps.length||r.geometry.arrowCrossings.length||r.nativeGeometry.outOfBounds.length||r.nativeGeometry.textOverlaps.length||r.nativeGeometry.arrowCrossings.length||!r.byteIdentical.svg||!r.byteIdentical.excalidraw);
 const audit={scope:'first 20 entries only',libraryVersion:version,browser:browser.version(),externalRequestsBlocked:true,canonicalSvgCount:report.length,canonicalExcalidrawCount:report.length,lessonLocalSvgCount:report.length,lessonLocalExcalidrawCount:report.length,totalArtifactCount:report.length*4,evidenceDirectory:evidence,errors,geometryFailures:failed.map(r=>r.file),visualReview:'Screenshots created; contact sheet review pending',limitations:['Native Arial text has no bold weight; source SVG is retained unchanged.','Cells intentionally smaller than general architecture-card guidelines: short numeric/node labels remain at 16px at native 500px SVG width.','Non-elbow arrows support native endpoint bindings; complex bends may need manual adjustment after large moves.'],diagrams:report};
 await fs.writeFile(process.env.DIAGRAM_AUDIT||path.join(here,'audit-first-half.json'),JSON.stringify(audit,null,2)+'\n');
 console.log(JSON.stringify({libraryVersion:version,diagrams:report.length,artifacts:report.length*4,errors,geometryFailures:failed.map(r=>({file:r.file,geometry:r.geometry})),evidence},null,2));
 if(errors.length||failed.length)process.exitCode=1;
}finally{await browser.close();await server.close()}
