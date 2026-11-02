export const C={bg:'#090D12',white:'#F1F1EB',muted:'#B5C0CD',line:'#53677A',faint:'#233242',teal:'#63E2C4',amber:'#F0BA76',violet:'#B9A2ED',red:'#EC8D96',blue:'#83BAEA'};
const clamp=x=>Math.max(0,Math.min(1,x));
const smooth=x=>{x=clamp(x);return x*x*x*(x*(x*6-15)+10)};
const ease=(t,a,b)=>smooth((t-a)/(b-a));
const lerp=(a,b,u)=>a+(b-a)*u;
const visible=(t,a,b,c,d)=>ease(t,a,b)*(1-ease(t,c,d));
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const n=x=>Number(x.toFixed(3));
const g=(s,opacity=1,transform='')=>`<g opacity="${n(clamp(opacity))}" transform="${transform}">${s}</g>`;
function text(s,x,y,size=28,color=C.white,opt={}){
 return `<text x="${n(x)}" y="${n(y)}" fill="${color}" font-size="${n(size)}" font-family="${opt.mono?'Menlo, monospace':opt.serif?'Georgia, serif':'Avenir Next, sans-serif'}" text-anchor="${opt.anchor??'middle'}" font-weight="${opt.bold?600:400}"${opt.italic?' font-style="italic"':''}>${esc(s)}</text>`;
}
function rect(x,y,w,h,stroke=C.line,fill=C.bg,sw=2,r=0){return `<rect x="${n(x)}" y="${n(y)}" width="${n(w)}" height="${n(h)}" rx="${r}" stroke="${stroke}" fill="${fill}" stroke-width="${sw}"/>`}
function line(x,y,x2,y2,color=C.line,sw=2){return `<path d="M ${x} ${y} L ${x2} ${y2}" stroke="${color}" stroke-width="${sw}" fill="none" stroke-linecap="round"/>`}
function linePathLength(d){
 const parts=d.match(/[MmLlHhVvZz]|-?\d*\.?\d+/g);let i=0,cmd='',x=0,y=0,sx=0,sy=0,length=0;
 while(i<parts.length){
   if(/[a-z]/i.test(parts[i]))cmd=parts[i++];
   const relative=cmd===cmd.toLowerCase(),kind=cmd.toUpperCase();
   if(kind==='Z'){length+=Math.hypot(x-sx,y-sy);x=sx;y=sy;cmd='';continue;}
   const a=+parts[i++];let nx=x,ny=y;
   if(kind==='H')nx=relative?x+a:a;
   else if(kind==='V')ny=relative?y+a:a;
   else {const b=+parts[i++];nx=relative?x+a:a;ny=relative?y+b:b;}
   if(kind==='M'){sx=nx;sy=ny;cmd=relative?'l':'L';}else length+=Math.hypot(nx-x,ny-y);
   x=nx;y=ny;
 }
 return Math.max(1,length);
}
function path(d,color=C.line,sw=2,progress=1){
 const length=linePathLength(d),q=clamp(progress);
 return `<path d="${d}" stroke="${color}" stroke-width="${sw}" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="${n(length)} ${n(length)}" stroke-dashoffset="${n((1-q)*length)}" opacity="${q<.0001?0:1}"/>`;
}
function circle(x,y,r,fill=C.white){return `<circle cx="${n(x)}" cy="${n(y)}" r="${r}" fill="${fill}"/>`}
function check(x,y,color=C.teal,q=1){return path(`M ${x-12} ${y} l 9 10 l 20 -25`,color,3.5,q)}
function cross(x,y,color=C.red,q=1){return path(`M ${x-10} ${y-10} l 20 20 M ${x+10} ${y-10} l -20 20`,color,3,q)}
function curvePoint(a,b,u,bend=0){const dx=b[0]-a[0],dy=b[1]-a[1],l=Math.hypot(dx,dy)||1;return[lerp(a[0],b[0],u)-dy/l*bend*Math.sin(Math.PI*u),lerp(a[1],b[1],u)+dx/l*bend*Math.sin(Math.PI*u)]}
function routePoint(points,u){let ds=points.slice(1).map((p,i)=>Math.hypot(p[0]-points[i][0],p[1]-points[i][1]));let d=clamp(u)*ds.reduce((a,b)=>a+b,0);for(let i=0;i<ds.length;i++){if(d<=ds[i]||i===ds.length-1)return[lerp(points[i][0],points[i+1][0],d/ds[i]),lerp(points[i][1],points[i+1][1],d/ds[i])];d-=ds[i]}return points[0]}
function routePath(points,color,sw=2,q=1){return path('M '+points.map(v=>v.join(' ')).join(' L '),color,sw,q)}
function block(x,y,color=C.teal,size=22,label=''){return rect(x-size/2,y-size/2,size,size,color,C.bg,2,2)+(label?text(label,x,y+size*.14,size*.3,color,{mono:true}):'')}
function traveling(points,u,color=C.teal,size=22){const[x,y]=routePoint(points,u);return block(x,y,color,size)}
function subtitle(s,t,a,b,c,d,color=C.muted){return g(text(s,800,812,32,color),visible(t,a,b,c,d))}
function intro(s,t){return g(text(s,800,139,48,C.white,{serif:true}),visible(t,0,.8,2.4,3.3))}
function camera(s,cx,cy,scale){return g(s,1,`translate(800 440) scale(${n(scale)}) translate(${-n(cx)} ${-n(cy)})`)}

export {clamp,smooth,ease,lerp,visible,g,text,rect,line,path,circle,check,cross,curvePoint,routePath,block,traveling,subtitle,intro,camera};
