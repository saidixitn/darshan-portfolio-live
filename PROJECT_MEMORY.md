# Darshan Naidu Portfolio · Master Project Memory & Architecture Guide

> **Permanent Memory File**: This document records all user instructions, technical decisions, architectural patterns, and design rules established for Darshan Naidu's creative portfolio.

---

## 1. Core Operating Protocols & Rules

### Git Policy
* **Strict Rule**: NEVER run `git push` or push changes to GitHub / remote repositories without explicit, verbal approval from the user.
* **Permitted**: Local development, running test servers (`http://localhost:8088`), inspecting files, and committing locally (`git commit`).
* **Deployments**: Only push to GitHub/Vercel when the user specifically writes "push to github" or "push to vercel".

### Local Verification
* All code, video playback, and layout changes must be verified locally before declaring complete.

---

## 2. Creator Profile & Brand Standards

* **Name**: Darshan Naidu
* **Discipline**: Creative Video Editor & Visual Designer
* **Location**: **Visakhapatnam (Vizag), Andhra Pradesh, India** *(Mandatory: Never omit or replace)*
* **Social Channels**:
  * Instagram: [`@fxdarshan`](https://www.instagram.com/fxdarshan/)
  * Email: `darshan@darshannaidu.com`
* **Creative Ethos**: *"Different interests. One creative space."*
  * High-retention pacing (pattern interrupts every 2.5s, strong visual hooks within 0.8s)
  * Dynamic sound design (layered ambient audio, riser builds, beat drops)
  * Kinetic typography and track-matte transitions
  * Brutalist graphic poster design

---

## 3. Video Archive Curation & Layout Hierarchy

On `/video-archive`:
1. **Hero Banner / Thumbnail Video**:
   * Remains **X-ENTI'ALL** (`/assets/videos/x-entiall.mp4`) with poster `/assets/videos/reels-1-poster.webp`.
2. **Reel Grid Starting Card**:
   * Must always be **Reel 2** (`/assets/videos/reels-2.mp4` in 9:16 vertical format).
   * **Rule**: X-ENTI'ALL must NEVER be Card #1 in the grid, to prevent duplicate video appearance at the top.
3. **Reel Grid Closing Card**:
   * **X-ENTI'ALL** is positioned as the final featured card (Card #11) in widescreen 16:9 format (`is-featured-16-9`).
4. **Current Array Order**:
   1. `reels-2.mp4` (vertical 9:16)
   2. `reels-3.mp4` (vertical 9:16)
   3. `reels-4.mp4` (vertical 9:16)
   4. `reels-7.mp4` (widescreen 16:9)
   5. `reels-6.mp4` (widescreen 16:9)
   6. `reels-8.mp4` (vertical 9:16)
   7. `reels-9.mp4` (vertical 9:16)
   8. `reels-10.mp4` (vertical 9:16)
   9. `reels-11.mp4` (vertical 9:16)
   10. `reels-12.mp4` (vertical 9:16)
   11. `reels-13.mp4` (vertical 9:16)
   12. `reels-5.mp4` (featured 16:9)
   13. `x-entiall.mp4` (featured 16:9)

---

## 4. High-Performance Video & Web Architecture

### 100% Free Edge Streaming
* Self-hosted on Vercel's global Edge CDN (`darshannaidu.vercel.app`) using HTTP 206 Partial Content (Byte-Range requests).
* No paid third-party infrastructure.

### Media Encoding
* All videos encoded with macOS `avconvert` as H.264 High-Profile with **FastStart enabled** (`moov` atom at the very start of the container before `mdat`).
* Enables browsers to begin decoding within ~250ms on the first byte range request without downloading the entire file.
* High-res WebP posters attached as CSS backgrounds and `poster` attributes on every card to eliminate black-box flashes.

### Elimination of Render Blocking
* **No `@import` in CSS**: Unused font imports (`DM Sans`, `Geist Mono`, `Inter`) must never exist in `assets/index-ZSMau8ex.css`.
* Local Satoshi font (`/assets/Satoshi-Variable-ChAXbpFa.ttf`) preloaded in `<head>` with `font-display: swap;`.
* Google Fonts loaded non-blockingly via `media="print" onload="this.media='all'"`.

### Video Preload Hygiene
* **Never use `<link rel="preload" as="video">` in `<head>`**: Causes Chromium to fetch the full file twice (GET + Range). Rely on `<video preload="auto" autoplay loop muted playsinline>`.

### Service Worker & Fast Loader Engine
* **`sw.js`**: Video streaming Service Worker caching byte-range slices for **0ms repeat playback** directly from local CacheStorage.
* **`assets/fast-loader.js`**: Speculative pre-warming engine triggering on 65ms hover/touch events for internal navigation links.
* **Preloader Duration**: Snappy 0.75s animation timing (down from 1.5s).

---

## 5. AI-Era (GEO) & Search Engine Optimization

### AI Search Discovery
* **`llms.txt`**: Spec-compliant overview for ChatGPT Search, Perplexity, Claude, Gemini, and Apple Intelligence.
* **`llms-full.txt`**: Exhaustive case study and project breakdown for AI agents.
* **`robots.txt`**: Explicitly authorizes AI bots (`GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`) and links to `sitemap.xml`.

### Schema.org Structured Data (JSON-LD)
* **Homepage**: `Person` & `WebSite` graph with `@fxdarshan` in `sameAs`.
* **Video Archive**: `CollectionPage` with `VideoObject` rich snippet items.
* **Poster Archive**: `ImageGallery` schema.
* **Works & About**: `CollectionPage` and `ProfilePage`.

### Metadata & PWA Standards
* Canonical `<link rel="canonical">` on every page.
* Theme color `<meta name="theme-color" content="#0b0b0c">`.
* PWA Web App Manifest (`site.webmanifest`).
* All `<img>` tags must have descriptive, human `alt` text. Never use blank `alt=""`.
