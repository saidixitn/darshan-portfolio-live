# Darshan Naidu · Creative Portfolio & Motion Architecture

[![Live Deployment](https://img.shields.io/badge/Production-darshannaidu.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://darshannaidu.vercel.app)
[![Hosting](https://img.shields.io/badge/Infrastructure-100%25%20Free%20Edge%20CDN-success?style=for-the-badge)](https://vercel.com)
[![Streaming](https://img.shields.io/badge/Streaming-HTTP%20206%20Partial%20Content-blue?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/206)
[![Performance](https://img.shields.io/badge/Service%20Worker-darshan--portfolio--v2-orange?style=for-the-badge)](./sw.js)
[![License](https://img.shields.io/badge/Creator-Darshan%20Naidu%20(Vizag)-purple?style=for-the-badge)](https://www.instagram.com/fxdarshan/)

> *"Different interests. One creative space."*  
> The official portfolio and video streaming platform for **Darshan Naidu**, Creative Video Editor, Visual Designer, and Motion Specialist based in **Visakhapatnam (Vizag), Andhra Pradesh, India**.

---

## ⚡ Quick Links & Navigation

| Route | Page File | Description |
| :--- | :--- | :--- |
| **`/`** | [`index.html`](./index.html) | Flagship landing experience: interactive kinetic lettermark, design manifesto, spotlight reel, and creative values. |
| **`/video-archive`** | [`video-archive.html`](./video-archive.html) | Curated video gallery showcasing 13+ high-retention commercial edits, vertical social cuts, and widescreen brand teasers. |
| **`/poster-archive`** | [`poster-archive.html`](./poster-archive.html) | Graphic design gallery featuring brutalist typography, sneaker art, and architectural poster experiments. |
| **`/works`** | [`works.html`](./works.html) | Horizontal work-selection slider highlighting major case studies with smooth transition physics. |
| **`/about`** | [`about.html`](./about.html) | Creative journey, biography, philosophy, aesthetic foundations, and contact links. |

---

## 🎬 Engineering Highlights

This portfolio is built to demonstrate not just visual excellence, but world-class web engineering. Unlike traditional portfolios that embed sluggish third-party iframe players (YouTube, Vimeo) or pay for expensive video CDNs, this platform runs on a **100% free, self-hosted, ultra-low-latency edge video architecture**.

```
                           [ Visitor Browser ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
      [ sw.js (Worker) ]                       [ fast-loader.js ]
     Byte-Range Slice Cache                   Speculative Pre-warm
     0ms Repeat Playback                      (65ms Hover / Touch)
              │                                         │
              └────────────────────┬────────────────────┘
                                   ▼
                      [ Vercel Edge Global CDN ]
                     HTTP 206 Partial Content
                    FastStart ISO Base Media MP4
```

### Key Technical Pillars

1. **Native HTTP 206 Partial Content**:
   - Every video is encoded as an ISO Base Media MP4 (H.264 High-Profile) with the **FastStart (`moov` atom)** placed at the very beginning of the container.
   - Browsers start streaming within ~250ms on the initial byte-range request without downloading multi-megabyte payloads up front.
2. **Zero Render-Blocking CSS & Modern Typography**:
   - No `@import` statements inside stylesheet bundles.
   - Local Satoshi variable font bundled in WOFF2/TTF formats with `font-display: swap;`.
   - Google Fonts loaded non-blockingly via print media swaps.
3. **Smart Service Worker Caching (`sw.js`)**:
   - Intercepts Range requests and caches initial video slices in `CacheStorage`.
   - Delivers **0ms instant replay** on return visits or looping video views.
4. **Speculative Pre-Warming Engine (`assets/fast-loader.js`)**:
   - Detects 65ms intent hovers and touch starts on navigation anchors.
   - Pre-warms upcoming page chunks and video files in `requestIdleCallback` before the user finishes clicking.
5. **Fluid Responsive Framing System**:
   - Pixel-perfect display across desktop (1440p, 4K), tablet, and mobile (iPhone, Android).
   - Dynamic 16:9 widescreen uncropped hero container, fluid typography with CSS `clamp()`, and guaranteed zero horizontal overflow (`scrollWidth === clientWidth`).

---

## 📁 Repository Structure

```
.
├── index.html                   # Flagship portfolio homepage
├── video-archive.html           # Dedicated video archive & reel gallery
├── poster-archive.html          # Graphic poster archive & typography showcase
├── works.html                   # Selected works interactive slider
├── about.html                   # Biography, design ethos, and contact
├── server.py                    # Local test server with clean URL rewrite routing
├── sw.js                        # Edge video caching Service Worker (v2)
├── site.webmanifest             # Native mobile PWA manifest
├── robots.txt                   # Crawler permissions & AI search index pointers
├── sitemap.xml                  # Canonical XML sitemap for Google & Bing
├── llms.txt                     # AI summary index (ChatGPT, Perplexity, Claude, Gemini)
├── llms-full.txt                # Full project documentation for AI crawlers
│
├── assets/                      # Production runtime bundles
│   ├── fast-loader.js           # Speculative pre-warming script
│   ├── index-CnbWzhzO.js        # Core GSAP timelines, Lenis scroll & reels gallery
│   ├── index-ZSMau8ex.css       # Core styles & responsive rules
│   ├── Satoshi-Variable-*.ttf   # Bundled local Satoshi variable font
│   ├── images/darshan/*.webp    # Compressed WebP kinetic wordmark letter tiles
│   └── videos/                  # H.264 FastStart MP4s + WebP posters
│       ├── x-entiall.mp4        # Hero campaign reel (Card 13 featured & hero banner)
│       ├── reels-2.mp4          # Reel Card 1 (Vertical 9:16)
│       ├── reels-3.mp4          # Reel Card 2 (Vertical 9:16)
│       ├── reels-4.mp4          # Reel Card 3 (Vertical 9:16)
│       ├── reels-5.mp4          # Reel Card 12 (Featured 16:9)
│       ├── reels-6.mp4          # Reel Card 5 (Widescreen 16:9)
│       ├── reels-7.mp4          # Reel Card 4 (Widescreen 16:9)
│       ├── reels-8.mp4          # Reel Card 6 (Vertical 9:16)
│       ├── reels-9.mp4          # Reel Card 7 (Vertical 9:16)
│       ├── reels-10.mp4         # Reel Card 8 (Vertical 9:16)
│       ├── reels-11.mp4         # Reel Card 9 (Vertical 9:16)
│       ├── reels-12.mp4         # Reel Card 10 (Vertical 9:16, new)
│       ├── reels-13.mp4         # Reel Card 11 (Vertical 9:16, new)
│       └── *-poster.webp        # Native extracted high-res WebP video posters
│
├── dist/                        # Production build mirror for deployment sync
│
└── [Documentation Suite]
    ├── README.md                # Project overview & navigation hub (this file)
    ├── VIDEO_GUIDE.md           # Video encoding, FastStart, poster generation & ingest
    ├── ARCHITECTURE.md          # GSAP physics, Lenis scroll, Service Worker & preloader
    ├── MOBILE_GUIDE.md          # Viewport breakpoints, framing fixes & responsive layout
    ├── SEO_GEO_GUIDE.md         # llms.txt, Schema.org JSON-LD, and AI discovery
    ├── DEPLOYMENT.md            # Git rules, local verification, and Vercel edge deployment
    ├── PROJECT_MEMORY.md        # Permanent architecture and design decisions
    └── GEMINI.md                # Master workspace rules & AI assistant memory
```

---

## 🛠️ Local Development & Quick Start

To preview the project locally with exact production routing (including extensionless clean URLs like `/video-archive` and `/works`):

```bash
# 1. Start the dedicated Python server with URL rewriting
python3 server.py

# 2. Open in your browser
open http://localhost:8088
```

> [!NOTE]
> Do not use standard `python3 -m http.server`, because it cannot resolve extensionless routes (e.g. `/video-archive` without `.html`), resulting in 404s. `server.py` includes custom routing that correctly maps extensionless requests.

---

## 📖 In-Depth Documentation Suite

For granular instructions and technical explanations, refer to the dedicated guides:

- 📹 **[Video Architecture & Ingestion Guide](./VIDEO_GUIDE.md)**: How to encode FastStart H.264 MP4s, generate WebP posters using native macOS Swift scripts without ffmpeg, and add new reels to the archive.
- ⚙️ **[Frontend Architecture Guide](./ARCHITECTURE.md)**: Deep dive into the GSAP timelines, Lenis smooth scrolling, the byte-range caching Service Worker, and anti-flash routing.
- 📱 **[Mobile Responsive Design Guide](./MOBILE_GUIDE.md)**: Detailed breakdown of the viewport scaling, 16:9 hero preservation, typography clamps, and 0-overflow guarantees.
- 🔍 **[SEO, GEO & Discovery Guide](./SEO_GEO_GUIDE.md)**: Complete guide to AI Search optimization (`llms.txt`), JSON-LD schemas, and crawler configs.
- 🚀 **[Deployment & Developer Workflow](./DEPLOYMENT.md)**: The strict Git deployment protocol, local headless test suites, and Vercel edge synchronization.

---

## 👤 Creator Profile

- **Creator**: Darshan Naidu
- **Role**: Creative Video Editor & Visual Designer
- **Location**: **Visakhapatnam (Vizag), Andhra Pradesh, India**
- **Instagram**: [`@fxdarshan`](https://www.instagram.com/fxdarshan/)
- **Email**: [`darshan@darshannaidu.com`](mailto:darshan@darshannaidu.com)
- **Live Portfolio**: [darshannaidu.vercel.app](https://darshannaidu.vercel.app)
