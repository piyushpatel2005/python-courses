// Reusable browser-side SVG-native conversion and actual editor acceptance.
// Pass to Playwright page.evaluate; window.E and window.api must be mounted.
export async function convertAndValidate({source,name}){
  const E=window.E; const svg=new DOMParser().parseFromString(source,'image/svg+xml').documentElement;
  const list=[];const cards=[];let serial=0;
  const n=(node,key,def=0)=>Number(node.getAttribute(key)??def);
  const base=(node,type)=>({id:'e'+(++serial),type,x:n(node,'x'),y:n(node,'y'),strokeColor:node.getAttribute('stroke')||'transparent',backgroundColor:node.getAttribute('fill')||'transparent',fillStyle:'solid',strokeWidth:n(node,'stroke-width',1),roughness:0,opacity:100,angle:0,groupIds:[],locked:false,roundness:null});
  function walk(node,group=null){
   const tag=node.tagName;
   if(['defs','title','desc'].includes(tag)) return;
   if(tag==='g'){
    const groupId='card-'+(++serial),members=[];
    for(const child of node.children){const el=walk(child,groupId);if(el)members.push(el);}
    const rect=members.find(e=>e.type==='rectangle');const texts=members.filter(e=>e.type==='text');
    cards.push(rect);
    // Excalidraw permits one bound text per container. Mixed-size cards use groups.
    if(texts.length===1){texts[0].containerId=rect.id;texts[0].verticalAlign='middle';rect.boundElements=[{id:texts[0].id,type:'text'}];}
    return;
   }
   let el;
   if(tag==='rect'){
    el={...base(node,'rectangle'),width:n(node,'width'),height:n(node,'height'),roundness:n(node,'rx')?{type:3}:null};
    if(!group)el.locked=true;
   }else if(tag==='text'){
    const size=n(node,'font-size',19),text=node.textContent;
    const canvas=document.createElement('canvas'),ctx=canvas.getContext('2d');ctx.font=size+'px Arial';
    const m=ctx.measureText(text),height=size*1.25;
    el={...base(node,'text'),x:n(node,'x')-m.width/2,y:n(node,'y')-size,width:m.width,height,text,originalText:text,fontSize:size,fontFamily:2,lineHeight:1.25,textAlign:'center',verticalAlign:'top',containerId:null,autoResize:true,strokeColor:node.getAttribute('fill'),backgroundColor:'transparent'};
   }else if(tag==='path' && node.hasAttribute('data-connector')){
    const coords=node.getAttribute('d').match(/-?\d+(?:\.\d+)?/g).map(Number);const points=[];
    for(let i=0;i<coords.length;i+=2)points.push([coords[i]-coords[0],coords[i+1]-coords[1]]);
    el={...base(node,'arrow'),x:coords[0],y:coords[1],width:Math.max(...points.map(p=>p[0]))-Math.min(...points.map(p=>p[0])),height:Math.max(...points.map(p=>p[1]))-Math.min(...points.map(p=>p[1])),points,startArrowhead:null,endArrowhead:node.getAttribute('data-arrow')==='true'?'triangle':null,startBinding:null,endBinding:null,elbowed:false};
   }
   if(el){if(group)el.groupIds=[group];list.push(el);return el;}
  }
  for(const node of svg.children)walk(node);
  for(const arrow of list.filter(e=>e.type==='arrow')){
   for(const [key,point] of [['startBinding',arrow.points[0]],['endBinding',arrow.points.at(-1)]]){
    const x=arrow.x+point[0],y=arrow.y+point[1];
    const card=cards.find(c=>x>=c.x-.1&&x<=c.x+c.width+.1&&y>=c.y-.1&&y<=c.y+c.height+.1&&(Math.abs(x-c.x)<.1||Math.abs(x-c.x-c.width)<.1||Math.abs(y-c.y)<.1||Math.abs(y-c.y-c.height)<.1));
    if(card){arrow[key]={elementId:card.id,focus:0,gap:0,fixedPoint:[(x-card.x)/card.width,(y-card.y)/card.height]};card.boundElements??=[];card.boundElements.push({id:arrow.id,type:'arrow'});}
   }
  }
  let elements=E.convertToExcalidrawElements(list,{regenerateIds:false});
  // Skeleton conversion measures text; retain SVG-centered placement with its true width.
  elements=elements.map(e=>{const src=list.find(s=>s.id===e.id);return {...e,...(e.type==='text'?{x:src.x+src.width/2-e.width/2,y:src.y}:{}),groupIds:src.groupIds,boundElements:src.boundElements||null,...(e.type==='arrow'?{startBinding:src.startBinding,endBinding:src.endBinding}:{}),updated:1,seed:1000+list.indexOf(src),versionNonce:1000+list.indexOf(src)};});
  const sourceTexts=[...svg.querySelectorAll('text')].map(e=>e.textContent);
  if(JSON.stringify(elements.filter(e=>e.type==='text').map(e=>e.originalText))!==JSON.stringify(sourceTexts))throw Error('Source text mismatch');
  if(elements.some(e=>!['text','rectangle','arrow'].includes(e.type)))throw Error('Unexpected non-editable element');
  const appState={viewBackgroundColor:'#ffffff',theme:'light',gridSize:null,exportBackground:true,exportWithDarkMode:false};
  const json=E.serializeAsJSON(elements,appState,{},'local');
  // Real file loader, then real React editor and SVG exporter, not just JSON parsing.
  const imported=await E.loadFromBlob(new Blob([json],{type:'application/vnd.excalidraw+json'}),null,null);
  window.api.updateScene({elements:imported.elements,appState});
  window.api.scrollToContent(imported.elements,{fitToContent:true});
  await new Promise(r=>setTimeout(r,100));
  const loaded=window.api.getSceneElements();
  if(loaded.length!==elements.length)throw Error('Dropped elements');
  const rendered=await E.exportToSvg({elements:loaded,appState,files:{},exportPadding:0});
  const text=loaded.find(e=>e.type==='text'&&!e.containerId);
  const edited=loaded.map(e=>e.id===text.id?{...e,text:e.text+' [EDIT TEST]',originalText:e.originalText+' [EDIT TEST]',version:e.version+1}:e);
  window.api.updateScene({elements:edited});
  const editExport=await E.exportToSvg({elements:window.api.getSceneElements(),appState,files:{},exportPadding:0});
  if(!editExport.textContent.includes('[EDIT TEST]'))throw Error('Text edit export failed');
  const editJson=E.serializeAsJSON(window.api.getSceneElements(),appState,{},'local');
  const reload=await E.loadFromBlob(new Blob([editJson]),null,null);
  if(!reload.elements.some(e=>e.text?.includes('[EDIT TEST]')))throw Error('Edited file reload failed');
  window.api.updateScene({elements:imported.elements,appState});
  const count=type=>loaded.filter(e=>e.type===type).length;
  return {json,render:rendered.outerHTML,editedRender:editExport.outerHTML,stats:{name,elements:loaded.length,text:count('text'),rectangles:count('rectangle'),arrows:count('arrow'),boundArrowEnds:loaded.filter(e=>e.type==='arrow').reduce((n,e)=>n+!!e.startBinding+!!e.endBinding,0),boundTexts:loaded.filter(e=>e.type==='text'&&e.containerId).length,groups:new Set(loaded.flatMap(e=>e.groupIds)).size,import:true,editorRender:true,textEditExport:true,editedFileReload:true}};
}
