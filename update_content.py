import subprocess

# 1. Update index-CnbWzhzO.js
with open("assets/index-CnbWzhzO.js", "r") as f:
    js = f.read()

# Update kt array descriptions & roles with punchy hooks
pos_kt = js.find("const kt=[")
pos_kt_end = js.find("];", pos_kt) + 2

new_kt = '''const kt=[{id:0,slug:"instagram-reels",title:`Rhythm & Motion,\\nInstagram Reels`,description:"High-energy video editing, relentless pacing, and kinetic storytelling designed for the infinite scroll. From punchy 9:16 vertical hooks to widescreen cinematic films, I turn raw footage into unforgettable visual experiences.",brand:"Instagram Reels",location:"India",role:`1 - Video Editing & Motion\\n2 - Creative Direction\\n3 - Social Media Strategy\\n4 - Sound & Color Grading`,year:"24-26",images:[{src:Pt("/work-section/slider_img_1.webp"),w:1920,h:1080}]},{id:1,slug:"poster-archive",title:`Visual Archive,\\nPoster Collection`,description:"Bold brutalist typography, cultural iconography, and high-impact print aesthetics. Exploring the intersection of sports culture, heritage architecture, and modern graphic design.",brand:"Poster Archive",location:"India",role:`1 - Visual Design\\n2 - Typography Direction\\n3 - Editorial & Brand Art\\n4 - Creative Curation`,year:"24-26",images:[{src:Pt("/work-section/slider_img_2.webp"),w:1888,h:1110}]}];'''

assert pos_kt != -1 and pos_kt_end != -1
js = js[:pos_kt] + new_kt + js[pos_kt_end:]

# Update video cards generation in rs() to remove ratio/badges/details and just keep Mute/Unmute & Play/Pause controls
pos_dt = js.find("dt.replaceChildren();")
pos_dt_end = js.find('const v=document.getElementById("project-page");', pos_dt)
assert pos_dt != -1 and pos_dt_end != -1

# Minimal, clean video cards: ONLY mute/unmute icon and pause/play toggle!
new_render = '''dt.replaceChildren();const m=()=>{mr()};if(o===0){const G=document.createElement("div");G.className="reels-gallery";const R=[{src:Pt("/assets/videos/reels-1.mp4"),cls:"is-featured-16-9"},{src:Pt("/assets/videos/reels-2.mp4"),cls:"is-vertical-9-16"},{src:Pt("/assets/videos/reels-3.mp4"),cls:"is-vertical-9-16"},{src:Pt("/assets/videos/reels-4.mp4"),cls:"is-vertical-9-16"},{src:Pt("/assets/videos/reels-5.mp4"),cls:"is-widescreen-16-9"},{src:Pt("/assets/videos/reels-6.mp4"),cls:"is-widescreen-16-9"}];R.forEach(k=>{const c=document.createElement("div");c.className="reel-card "+k.cls;const V=document.createElement("video");V.src=k.src;V.autoplay=!0;V.loop=!0;V.muted=!0;V.playsInline=!0;V.setAttribute("playsinline","");V.setAttribute("webkit-playsinline","");V.oncanplay=m;V.onerror=m;setTimeout(m,300);const O=document.createElement("div");O.className="reel-card-overlay";const CTRLS=document.createElement("div");CTRLS.className="reel-minimal-controls";const PB=document.createElement("button");PB.className="reel-ctrl-btn reel-play-btn";PB.setAttribute("aria-label","Play or Pause");PB.innerHTML='<svg class="icon-pause" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg><svg class="icon-play" style="display:none;" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>';const MB=document.createElement("button");MB.className="reel-ctrl-btn reel-mute-btn";MB.setAttribute("aria-label","Mute or Unmute");MB.innerHTML='<svg class="icon-muted" viewBox="0 0 24 24"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg><svg class="icon-unmuted" style="display:none;" viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>';const syncPlay=()=>{const isP=V.paused;PB.querySelector(".icon-pause").style.display=isP?"none":"block";PB.querySelector(".icon-play").style.display=isP?"block":"none"};const syncMute=()=>{const isM=V.muted;MB.querySelector(".icon-muted").style.display=isM?"block":"none";MB.querySelector(".icon-unmuted").style.display=isM?"none":"block"};PB.onclick=e=>{e.stopPropagation();V.paused?V.play():V.pause();syncPlay()};MB.onclick=e=>{e.stopPropagation();V.muted=!V.muted;syncMute()};c.onclick=()=>{V.paused?V.play():V.pause();syncPlay()};CTRLS.appendChild(PB);CTRLS.appendChild(MB);O.appendChild(CTRLS);c.appendChild(V);c.appendChild(O);G.appendChild(c)});dt.appendChild(G)}else{const P=document.createElement("div");P.className="pinterest-gallery";const D=[{src:Pt("/projects/Itmatters/gallery/taj-mahal.webp"),title:"Taj Mahal — Marble Symphony",category:"Architecture / Heritage"},{src:Pt("/projects/Itmatters/gallery/virat-kohli.webp"),title:"Virat Kohli — Relentless Focus",category:"Sports / Editorial"},{src:Pt("/projects/Itmatters/gallery/bengaluru.webp"),title:"Bengaluru — Modernist Grid",category:"City Archive"},{src:Pt("/projects/Itmatters/gallery/darshan-mind.webp"),title:"Mind State — Studio Portrait",category:"Portraiture"},{src:Pt("/projects/Itmatters/gallery/humayuns-tomb.webp"),title:"Humayun\'s Tomb — Geometry",category:"Heritage"},{src:Pt("/projects/Itmatters/gallery/chennai.webp"),title:"Chennai — Coastal Pulse",category:"City Archive"},{src:Pt("/projects/Itmatters/gallery/mumbai.webp"),title:"Mumbai — Maximum Energy",category:"City Archive"},{src:Pt("/projects/Itmatters/gallery/time.webp"),title:"Time — Brutalist Chronology",category:"Graphic Study"},{src:Pt("/projects/Itmatters/gallery/darshan-original.webp"),title:"Darshan Naidu — Full Stance",category:"Portraiture"},{src:Pt("/projects/Itmatters/gallery/orange.webp"),title:"Citrus — High-Contrast Kinetic",category:"Color Study"},{src:Pt("/projects/Itmatters/gallery/neymar-jr.webp"),title:"Neymar Jr — Samba In Motion",category:"Sports / Typography"},{src:Pt("/projects/Itmatters/gallery/golden-temple.webp"),title:"Golden Temple — Sacred Light",category:"Heritage"},{src:Pt("/projects/Itmatters/gallery/darshan-creative.webp"),title:"Darshan Naidu — Creative Light",category:"Portraiture"},{src:Pt("/projects/Itmatters/gallery/hawa-mahal.webp"),title:"Hawa Mahal — 953 Casements",category:"Architecture"},{src:Pt("/projects/Itmatters/gallery/kolkata.webp"),title:"Kolkata — Howrah Twilight",category:"City Archive"},{src:Pt("/projects/Itmatters/gallery/qutub-minar.webp"),title:"Qutub Minar — Fluted Tower",category:"Heritage"}];D.forEach(p=>{const c=document.createElement("div");c.className="pinterest-card";const I=document.createElement("img");I.src=p.src;I.alt=p.title;I.loading="lazy";I.decoding="async";I.onload=m;I.onerror=m;const M=document.createElement("div");M.className="pinterest-card-meta";const S=document.createElement("span");S.className="pinterest-card-title";S.textContent=p.title;const C=document.createElement("span");C.className="pinterest-card-category";C.textContent=p.category;M.appendChild(S);M.appendChild(C);c.appendChild(I);c.appendChild(M);P.appendChild(c)});dt.appendChild(P)}const CTA=document.createElement("div");CTA.className="project-ig-banner";CTA.innerHTML='<a href="https://www.instagram.com/fxdarshan/" target="_blank" rel="noopener noreferrer" class="project-ig-btn"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg><span>Connect on Instagram @fxdarshan</span><span class="ig-arrow">↗</span></a>';dt.appendChild(CTA);'''

js = js[:pos_dt] + new_render + js[pos_dt_end:]

with open("/tmp/test_eval.js", "w") as tf:
    tf.write(js)

res = subprocess.run(["node", "--input-type=module", "-e", """
import fs from 'fs';
const c = fs.readFileSync('/tmp/test_eval.js', 'utf8');
import('data:text/javascript,' + encodeURIComponent(c)).catch(e => {
  if (e instanceof SyntaxError) {
    console.error('SYNTAX ERROR:', e.message);
    process.exit(1);
  }
});
"""], capture_output=True, text=True)

if res.returncode != 0:
    print("❌ JS syntax error:", res.stderr)
    exit(1)

with open("assets/index-CnbWzhzO.js", "w") as f:
    f.write(js)
print("✅ assets/index-CnbWzhzO.js updated and syntax verified!")

