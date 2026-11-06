# Darshan Naidu Portfolio · Master Workspace Rules & Project Memory

This document is the authoritative memory file for Antigravity and any AI assistant operating in this repository. It preserves all user instructions, architectural decisions, design rules, and performance protocols established for **Darshan Naidu's Creative Portfolio**.

---

## 1. Absolute Golden Rules (Never Break)

### Git & Deployment Protocol
- **STRICT FORBIDDEN**: Never run `git push` or push changes to GitHub / remote repositories without explicit, verbal approval from the user.
- **Allowed**: Making local code changes, running local test servers (`http://localhost:8088`), and creating local `git commit`s.
- **Push Workflow**: Only when the user explicitly instructs to *"push to github"* or *"push to vercel"* may `git push origin main` be executed.

### Local Verification First
- Always test and verify code, layouts, and performance in the local environment first before declaring work complete.

---

## 2. Creator Identity & Content Fidelity

- **Name**: Darshan Naidu
- **Title**: Creative Video Editor & Visual Designer
- **Location**: **Visakhapatnam (Vizag), Andhra Pradesh, India** (STRICT: Never change or omit this location).
- **Instagram**: `@fxdarshan` (URL: `https://www.instagram.com/fxdarshan/`)
- **Email**: `darshan@darshannaidu.com`
- **Brand Ethos**: *"Different interests. One creative space."* Focus on retention-driven pacing, kinetic typography, dynamic sound design, and brutalist graphic poster design.

---

## 3. Video Archive Layout & Sequence Rules

On `/video-archive` (`video-archive.html`):
1. **Top Hero Thumbnail Video**:
   - Must remain **X-ENTI'ALL** (`/assets/videos/x-entiall.mp4` with poster `/assets/videos/reels-1-poster.webp`).
2. **First Reel Card in Grid**:
   - Must be **Reel 2** (`/assets/videos/reels-2.mp4` in vertical 9:16 format).
   - **RULE**: Never place X-ENTI'ALL as Card #1 right under the hero banner, to prevent duplicate appearance at the top.
3. **End of Archive**:
   - **X-ENTI'ALL** is positioned as the final featured card (Card #11) in widescreen 16:9 format (`is-featured-16-9`).
4. **Current Array Order**:
   - Card 1: `reels-2.mp4` (vertical 9:16)
   - Card 2: `reels-3.mp4` (vertical 9:16)
   - Card 3: `reels-4.mp4` (vertical 9:16)
   - Card 4: `reels-7.mp4` (widescreen 16:9)
   - Card 5: `reels-6.mp4` (widescreen 16:9)
   - Card 6: `reels-8.mp4` (vertical 9:16)
   - Card 7: `reels-9.mp4` (vertical 9:16)
   - Card 8: `reels-10.mp4` (vertical 9:16)
   - Card 9: `reels-11.mp4` (vertical 9:16)
   - Card 10: `reels-12.mp4` (vertical 9:16)
   - Card 11: `reels-13.mp4` (vertical 9:16)
   - Card 12: `reels-5.mp4` (featured 16:9)
   - Card 13: `x-entiall.mp4` (featured 16:9)

---

## 4. Performance & Video Streaming Architecture

### 100% Free & Self-Hosted Infrastructure
- All streaming runs directly on Vercel's Edge CDN (`darshannaidu.vercel.app`) using HTTP 206 Partial Content (Range requests).
- No paid third-party platforms or external video CDNs.

### Video Encoding Requirements
- All videos must be ISO Base Media MP4 (H.264 High-Profile) with **FastStart enabled** (`moov` atom at the very beginning of the container before `mdat`).
- Videos must have high-res WebP posters attached as CSS backgrounds and `poster` attributes to prevent any black-box flashing.

### Zero Render-Blocking Rules
- **NEVER** use `@import` inside CSS files (`assets/index-ZSMau8ex.css`). Unused fonts (DM Sans, Geist Mono, Inter) must never be imported.
- Local Satoshi font (`/assets/Satoshi-Variable-ChAXbpFa.ttf`) is preloaded in `<head>` and defined with `font-display: swap;`.
- Google Fonts must be loaded non-blockingly using `media="print" onload="this.media='all'"`.

### No Duplicate Video Preloads
- Do **NOT** use `<link rel="preload" as="video">` in `<head>`. Modern browsers download the entire file via GET on `<link preload>` and simultaneously open Range requests on `<video>`, causing duplicate bandwidth waste.
- Rely on `<video preload="auto" autoplay loop muted playsinline>` which manages byte ranges cleanly.

### Service Worker & Fast Loader Engine
- **`sw.js`**: Video streaming service worker that handles HTTP 206 Range requests and caches initial video bytes in `CacheStorage` for **0ms repeat playback**.
- **`assets/fast-loader.js`**: Speculative pre-warming script that listens for 65ms hover/touch events on navigation links and pre-warms upcoming video reels in `requestIdleCallback`.
- **Preloader Duration**: Kept at **0.75s** maximum. Never inflate counter duration back to 1.5s+.

---

## 5. Modern SEO & AI-Era (GEO) Standards

### AI Search Indexing
- **`llms.txt` & `llms-full.txt`**: Authoritative markdown indexes for ChatGPT Search, Perplexity, Claude, Gemini, and Apple Intelligence.
- **`robots.txt`**: Explicitly allows AI crawlers (`GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`) and points to `https://darshannaidu.vercel.app/sitemap.xml`.

### Schema.org Structured Data (JSON-LD)
Every page must have valid JSON-LD schemas:
- Homepage: `Person` & `WebSite` graph with `sameAs: ["https://www.instagram.com/fxdarshan/"]`.
- Video Archive: `CollectionPage` with `VideoObject` items.
- Poster Archive: `ImageGallery` schema.
- Works: `CollectionPage`.
- About: `ProfilePage`.

### Metadata & Mobile Standards
- Every HTML file must have:
  - `<link rel="canonical" href="..." />`
  - `<meta name="theme-color" content="#0b0b0c" />`
  - `<link rel="manifest" href="/site.webmanifest" />`
  - `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />`
  - All `<img>` tags must have descriptive, human, and keyword-rich `alt` text. Never leave empty `alt=""`.

---

## 6. Directory Structure & Key Files

```
├── GEMINI.md                    # This persistent master memory & rules file
├── llms.txt                     # AI discovery summary
├── llms-full.txt                # AI exhaustive project documentation
├── robots.txt                   # Crawler directives & sitemap reference
├── sitemap.xml                  # Video & image XML sitemap
├── site.webmanifest             # Native mobile PWA manifest
├── sw.js                        # Video streaming Service Worker
├── assets/
│   ├── fast-loader.js           # Speculative pre-warming engine
│   ├── index-CnbWzhzO.js        # Main GSAP timeline & video gallery logic
│   ├── index-ZSMau8ex.css       # Core styles (no render-blocking @import)
│   ├── Satoshi-Variable-*.ttf   # Bundled local Satoshi font (swap enabled)
│   ├── images/darshan/*.webp    # Compressed WebP kinetic letter tiles
│   └── videos/                  # H.264 FastStart optimized reels
├── index.html                   # Homepage
├── video-archive.html           # Video Archive
├── poster-archive.html          # Poster Archive
├── works.html                   # Selected Works
├── about.html                   # About Page
└── dist/                        # Production build mirror
```
