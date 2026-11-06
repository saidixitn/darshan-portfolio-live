# Deployment, Verification & Developer Protocol Guide

> **Operations Manual**: Standard operating procedures, Git governance rules, local testing pipelines, and Vercel edge deployment workflows for **Darshan Naidu's Portfolio**.

---

## 📑 Table of Contents

1. [The Golden Git Protocol](#1-the-golden-git-protocol)
2. [Creator Identity & Invariant Rules](#2-creator-identity--invariant-rules)
3. [Local Development & The `server.py` Routing Engine](#3-local-development--the-serverpy-routing-engine)
4. [Headless Verification Testing Suite](#4-headless-verification-testing-suite)
5. [GitHub & Vercel Edge Deployment Pipeline](#5-github--vercel-edge-deployment-pipeline)
6. [Cache Invalidation & Service Worker Life Cycle](#6-cache-invalidation--service-worker-life-cycle)
7. [Troubleshooting Common Issues](#7-troubleshooting-common-issues)

---

## 1. The Golden Git Protocol

This repository adheres to a strict Git safety protocol:

> [!CAUTION]
> ### The Absolute Golden Rule
> **NEVER** run `git push` or push changes to GitHub / remote repositories without **explicit, verbal approval from the user**.

### What is Permitted Locally:
- Editing files, creating assets, and updating stylesheets.
- Running the local test server on `http://localhost:8088`.
- Running headless browser tests and automated verification scripts.
- Creating local Git commits (`git commit -m "..."`).

### The Push Workflow:
Only when the user explicitly instructs to:
- *"push to github"*
- *"push to vercel"*
- *"push everything"*
- Or gives verbal approval (e.g. *"cool check everything and if alright then push"*)

May `git push origin main` be executed.

---

## 2. Creator Identity & Invariant Rules

Whenever modifying text, metadata, schemas, or documentation, the following creator facts are **permanent invariants**:

- **Name**: Darshan Naidu
- **Title**: Creative Video Editor & Visual Designer
- **Location**: **Visakhapatnam (Vizag), Andhra Pradesh, India**  
  *(STRICT: Never change to another city, never abbreviate away Andhra Pradesh in schemas, never omit India).*
- **Instagram**: [`@fxdarshan`](https://www.instagram.com/fxdarshan/) (URL: `https://www.instagram.com/fxdarshan/`)
- **Email**: `darshan@darshannaidu.com`
- **Brand Ethos**: *"Different interests. One creative space."*

---

## 3. Local Development & The `server.py` Routing Engine

Production Vercel servers automatically resolve clean, extensionless URLs (e.g., requests to `/video-archive` serve `video-archive.html`).

If a developer runs standard `python3 -m http.server`, the browser will return a **404 Not Found** because standard Python HTTP servers look for a directory named `video-archive/`.

### The Custom `server.py` Engine
This repository includes a dedicated `server.py` script that handles:
1. **Extensionless Route Rewrites**: Maps `/video-archive` to `video-archive.html`, `/works` to `works.html`, etc.
2. **Byte-Range Support (HTTP 206)**: Serves video slices accurately with `Accept-Ranges: bytes`.
3. **CORS & Cache Headers**: Sets development-friendly headers to prevent caching while testing.

```bash
# Start local development server
python3 server.py
# Running on http://localhost:8088
```

---

## 4. Headless Verification Testing Suite

Before committing or pushing any update, run the automated headless Chrome CDP test suite. This script validates that:
- 0 JavaScript console errors occur.
- 0 network requests fail (404/500).
- All video elements mount and resolve their media sources.
- No horizontal scrollbars exist on mobile viewports.

### Running the Test Suite

```bash
# Run headless browser verification
node -e "
import { spawn } from 'node:child_process';
import http from 'node:http';

async function test() {
  const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
    '--headless=new', '--remote-debugging-port=9222', 'about:blank'
  ]);
  // Connect via native WebSocket CDP and assert 0 errors...
}
test();
"
```

---

## 5. GitHub & Vercel Edge Deployment Pipeline

```
[ Local Verified Commits ]
           │
           ▼ (User Verbal Approval)
   `git push origin main`
           │
           ▼
[ GitHub Repository: saidixitn/darshan-portfolio-live ]
           │
           ▼ (Automated Webhook)
  [ Vercel Global Edge CDN ]
  - Edge Cache Invalidation
  - Global Anycast CDN Distribution
  - Production Live at darshannaidu.vercel.app
```

### The `dist/` Mirror Protocol
The repository contains both root files (`index.html`, `video-archive.html`, `assets/`) and a `dist/` mirror. 

Whenever modifying assets in `assets/` or root HTML files, **always mirror the changes to `dist/`**:
```bash
# Example sync after updating styles or videos
cp assets/videos/reels-* dist/assets/videos/
cp assets/index-*.js dist/assets/
cp assets/index-*.css dist/assets/
cp sw.js dist/sw.js
```

---

## 6. Cache Invalidation & Service Worker Life Cycle

Browsers aggressively cache CSS, fonts, and Service Workers. To ensure that users on mobile and desktop receive layout updates immediately:

### Step 1: Bump Cache Name
In both `sw.js` and `dist/sw.js`, increment the cache version constant:
```javascript
// Example: bump from v1 to v2
const CACHE_NAME = 'darshan-portfolio-v2';
```

### Step 2: Automatic Purge on Client
When a visitor opens the portfolio:
1. The browser checks `sw.js` in the background.
2. The Service Worker installs and fires the `activate` event.
3. The `activate` handler iterates through `caches.keys()`, compares each cache to `CACHE_NAME`, and deletes all outdated caches (`darshan-portfolio-v1`).
4. On the next fetch, all CSS and video assets are pulled fresh from the edge.

---

## 7. Troubleshooting Common Issues

### 1. `BrokenPipeError: [Errno 32] Broken pipe` in `server.py`
- **Cause**: When a browser starts buffering a video, it opens a Range request. If the user navigates away or the video loop restarts, the browser closes the socket while the Python server is still streaming bytes.
- **Impact**: Completely harmless. Normal browser behavior for media streaming.

### 2. Live Vercel returns 404 for a newly added video for ~10 seconds
- **Cause**: Vercel’s global Edge CDN propagates multi-megabyte binary files across hundreds of edge locations worldwide.
- **Resolution**: Wait 10–15 seconds for edge convergence. Subsequent requests will return `HTTP/2 200 OK` with `x-vercel-cache: HIT`.

### 3. Mobile screen scrolls sideways accidentally
- **Cause**: An element has an unconstrained pixel width or margin exceeding `390px`.
- **Resolution**: Check `MOBILE_GUIDE.md` and ensure `max-width: 100vw; overflow-x: hidden;` is preserved on root containers.
