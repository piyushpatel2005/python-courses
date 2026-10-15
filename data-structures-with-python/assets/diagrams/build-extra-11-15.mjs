import { convertAndValidate } from './second-half-native.mjs';
// Local-only SVG -> editable Excalidraw converter and real-library acceptance test.
// Dependencies live in scratch; see EDITING-EXCALIDRAW.md. Never writes existing SVGs.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
const here = path.dirname(fileURLToPath(import.meta.url));
const deps = process.env.EXCALIDRAW_DEPS || path.join(process.env.HOME, '.hermes/profiles/curriculum-dev/cache/scratch/oop-excalidraw');
const scratch = process.env.EXCALIDRAW_SCRATCH || path.join(process.env.HOME, '.hermes/profiles/curriculum-dev/cache/scratch/ds-extra-11-15');
await fs.mkdir(scratch,{recursive:true});
try { await fs.symlink(path.join(deps,'node_modules'),path.join(scratch,'node_modules'),'dir'); } catch(e) { if(e.code!=='EEXIST')throw e; }
const require = createRequire(path.join(scratch, 'package.json'));
const { chromium } = require('playwright');
const { createServer } = await import(require.resolve('vite'));
await fs.mkdir(path.join(scratch,'evidence'), {recursive:true});
await fs.writeFile(path.join(scratch,'index.html'), '<html><body><div id="root" style="width:1000px;height:1200px"></div><script type="module" src="/harness.jsx"></script></body></html>');
await fs.writeFile(path.join(scratch,'harness.jsx'), `import React from 'react';
import {createRoot} from 'react-dom/client';
import * as E from '@excalidraw/excalidraw';
import '@excalidraw/excalidraw/index.css';
window.E=E;
createRoot(document.getElementById('root')).render(<E.Excalidraw excalidrawAPI={api=>window.api=api}/>);`);
const server = await createServer({root:scratch,configFile:false,server:{host:'127.0.0.1',port:0,fs:{allow:[scratch,deps]}},logLevel:'error'});
await server.listen();
const browser = await chromium.launch({headless:true,channel:'chrome'});
try {
const page = await browser.newPage({viewport:{width:1050,height:1250}});
const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
// No course content may leave localhost, including font/network fallbacks.
await page.route('**/*',route=>new URL(route.request().url()).hostname==='127.0.0.1'?route.continue():route.abort());
await page.goto(server.resolvedUrls.local[0]);
await page.waitForFunction(()=>window.api && window.E);
const placements = JSON.parse(await fs.readFile(path.join(here,'placements-extra-11-15.json'),'utf8'));
if(placements.length!==40) throw Error('Expected forty placements');
const report=[];
for(const placement of placements){
 const source=await fs.readFile(path.join(here,placement.file),'utf8');
 const name=placement.file.replace('.svg','.excalidraw');
 const result=await page.evaluate(convertAndValidate,{source,name});
 const native=JSON.parse(result.json).elements;
 const texts=native.filter(e=>e.type==='text');
 const overlaps=[];
 for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){
   const a=texts[i],b=texts[j];
   if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1 && Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1)overlaps.push([a.text,b.text]);
 }
 const clipped=texts.filter(e=>e.x<0||e.y<0||e.x+e.width>600||e.y+e.height>900);
 if(overlaps.length||clipped.length)throw Error(name+' native geometry '+JSON.stringify({overlaps,clipped}));
 result.stats.nativeTextBoundsPass=true;result.stats.nativeTextNonOverlapPass=true;
 const local=path.resolve(here,'../..',placement.lesson,name);
 await fs.access(path.dirname(local));
 await fs.writeFile(path.join(here,name),result.json+'\n');await fs.writeFile(local,result.json+'\n');
 if((await fs.readFile(local,'utf8'))!==(await fs.readFile(path.join(here,name),'utf8')))throw Error('Copy mismatch');
 const stem=name.replace('.excalidraw','');
 await fs.writeFile(path.join(scratch,'evidence',stem+'.svg'),result.render);
 await fs.writeFile(path.join(scratch,'evidence',stem+'-edited.svg'),result.editedRender);
 await page.screenshot({path:path.join(scratch,'evidence',stem+'-editor.png')});
 const preview=await browser.newPage({viewport:{width:520,height:1100},deviceScaleFactor:1});
 await preview.setContent('<html><body style="margin:10px">'+source.replace('<svg ', '<svg style="width:500px;height:auto" ')+'</body></html>');
 const layout=await preview.evaluate(()=>{const svg=document.querySelector('svg'),vb=svg.viewBox.baseVal;const texts=[...svg.querySelectorAll('text')].map(e=>({text:e.textContent,b:e.getBBox()}));const clipped=texts.filter(({b})=>b.x<0||b.y<0||b.x+b.width>vb.width||b.y+b.height>vb.height).map(e=>e.text);const overlaps=[];for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){const a=texts[i].b,b=texts[j].b;if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>1)overlaps.push([texts[i].text,texts[j].text]);}return {clipped,overlaps};});
 if(layout.clipped.length||layout.overlaps.length)throw Error(stem+' text geometry '+JSON.stringify(layout));
 result.stats.svgTextBoundsPass=true;result.stats.svgTextNonOverlapPass=true;
 await preview.locator('svg').screenshot({path:path.join(scratch,'evidence',stem+'-500px.png')});
 await preview.close();
 if((await fs.readFile(path.join(here,placement.file),'utf8'))!==(await fs.readFile(path.resolve(here,'../..',placement.lesson,placement.file),'utf8')))throw Error('SVG copy mismatch');
 report.push({...result.stats,source:path.join(here,name),lesson:local,byteIdentical:true,svgByteIdentical:true,svgPreview:path.join(scratch,'evidence',stem+'-500px.png'),editorScreenshot:path.join(scratch,'evidence',stem+'-editor.png')});
}
if(errors.length)throw Error(errors.join('\n'));
const version=JSON.parse(await fs.readFile(path.join(scratch,'node_modules/@excalidraw/excalidraw/package.json'),'utf8')).version;
const checks=JSON.parse(await fs.readFile(path.join(here,'checks-extra-11-15.json'),'utf8'));
const audit={libraryVersion:version,browser:browser.version(),externalRequestsBlocked:true,canonicalSVG:40,canonicalEditable:40,lessonSVG:40,lessonEditable:40,algorithmChecks:checks,diagrams:report};
await fs.writeFile(path.join(scratch,'evidence','report.json'),JSON.stringify(audit,null,2));
await fs.writeFile(path.join(here,'audit-extra-11-15.json'),JSON.stringify(audit,null,2)+'\n');
console.log(JSON.stringify({libraryVersion:version,files:report.length*2,elements:report.reduce((n,r)=>n+r.elements,0),evidence:path.join(scratch,'evidence'),diagrams:report},null,2));
}finally{await browser.close();await server.close();}
