import fs from 'node:fs/promises';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {createHash} from 'node:crypto';
import sharp from 'sharp';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
import {memoryScenes} from './source/memory.mjs';
import repack from './source/repack.mjs';
import speculation from './source/speculation.mjs';
import prefetch from './source/prefetch.mjs';
import flint from './source/flint.mjs';
import {C} from './source/drawing.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const scratch=await fs.mkdtemp(path.join(os.tmpdir(),'homelab-animations-'));
const media=path.join(root,'docs/media');
const scenes=[...memoryScenes,prefetch,speculation,flint,repack];
const id=process.argv.slice(2).find(arg=>!arg.startsWith('--'));
const selected=scenes.filter(s=>!id||s.id===id);
const ffmpeg=process.argv.includes('--stills')?null:(process.env.FFMPEG||'ffmpeg');
const manifestPath=path.join(media,'manifest.json');
let manifest={format:'README animation exports',clips:[]};
try{manifest=JSON.parse(await fs.readFile(manifestPath,'utf8'));}catch(error){if(error.code!=='ENOENT')throw error;}

function svg(scene,t){return `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1600 900"><rect width="1600" height="900" fill="${C.bg}"/>${scene.frame(t)}</svg>`;}
async function run(args){
  const child=spawn(ffmpeg,['-hide_banner','-loglevel','error','-y',...args],{stdio:['ignore','inherit','inherit']});
  const [code]=await once(child,'exit');
  if(code!==0)throw Error(`ffmpeg exited ${code}`);
}
await fs.mkdir(media,{recursive:true});
await fs.mkdir(path.join(scratch,'checks'),{recursive:true});
for(const scene of selected){
  await fs.writeFile(path.join(media,scene.id+'.svg'),svg(scene,scene.poster));
  await sharp(Buffer.from(svg(scene,scene.poster))).png().toFile(path.join(media,scene.id+'.png'));
  for(const t of scene.checks) await sharp(Buffer.from(svg(scene,t))).resize(960,540).png().toFile(path.join(scratch,'checks',`${scene.id}-${t}.png`));
  if(!ffmpeg)continue;
  const mp4=path.join(media,scene.id+'.mp4');
  const child=spawn(ffmpeg,['-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','png','-framerate','60','-i','pipe:0','-an','-c:v','libx264','-threads','2','-preset','fast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',mp4],{stdio:['pipe','inherit','inherit']});
  child.stdin.on('error',()=>{});
  const ended=once(child,'exit');
  let previousSvg,previousFrame;
  for(let i=0;i<scene.duration*60;i++){
    const markup=svg(scene,i/60);
    if(markup!==previousSvg){
      previousFrame=await sharp(Buffer.from(markup)).png().toBuffer();
      previousSvg=markup;
    }
    const frame=previousFrame;
    if(!child.stdin.write(frame))await once(child.stdin,'drain');
  }
  child.stdin.end();
  const [code]=await ended;
  if(code!==0)throw Error(`Render failed: ${scene.id}`);
  await run(['-i',mp4,'-filter_complex',`[0:v]fps=25,split[a][b];[a]palettegen=max_colors=${scene.gifColors||192}:stats_mode=diff[p];[b][p]paletteuse=dither=${scene.gifDither||'bayer'}:bayer_scale=3:diff_mode=rectangle`,'-loop','0',path.join(media,scene.id+'.gif')]);
  const gif=await fs.stat(path.join(media,scene.id+'.gif'));
  const bytes=await fs.readFile(path.join(media,scene.id+'.gif'));
  const entry={id:scene.id,title:scene.title,primary:scene.id!=='repack-eight-rows',durationSeconds:scene.duration,width:bytes.readUInt16LE(6),height:bytes.readUInt16LE(8),gifFps:25,mp4Fps:60,frames:scene.duration*25,gifBytes:gif.size,gifSha256:createHash('sha256').update(bytes).digest('hex')};
  const entries=new Map((manifest.clips||[]).map(clip=>[clip.id,clip]));
  entries.set(scene.id,entry);
  manifest.clips=scenes.map(clip=>entries.get(clip.id)).filter(Boolean);
  await fs.writeFile(manifestPath,JSON.stringify(manifest,null,2)+'\n');
  console.log(`${scene.id}: ${scene.duration}s, 1920×1080, 25 fps GIF, ${(gif.size/1048576).toFixed(2)} MiB`);
}
