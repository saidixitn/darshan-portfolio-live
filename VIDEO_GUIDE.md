# Video Architecture & Reel Ingestion Guide

> **Authoritative Technical Manual**: A comprehensive guide to the video streaming architecture, FastStart encoding protocols, native frame extraction, and video ingestion pipeline powering **Darshan Naidu's Portfolio**.

---

## 📑 Table of Contents

1. [Architectural Overview](#1-architectural-overview)
2. [The FastStart Atom Principle](#2-the-faststart-atom-principle)
3. [Zero-Black-Box Poster Strategy](#3-zero-black-box-poster-strategy)
4. [Native Frame Extraction (No ffmpeg Needed)](#4-native-frame-extraction-no-ffmpeg-needed)
5. [HTTP 206 Partial Content & Edge Range Requests](#5-http-206-partial-content--edge-range-requests)
6. [Why `<link rel="preload" as="video">` is Forbidden](#6-why-link-relpreload-asvideo-is-forbidden)
7. [Step-by-Step: Adding a New Reel to the Archive](#7-step-by-step-adding-a-new-reel-to-the-archive)
8. [Current Video Catalog & Sequence Rules](#8-current-video-catalog--sequence-rules)

---

## 1. Architectural Overview

Traditional video portfolios suffer from two main flaws:
1. **Third-Party Iframe Embeds (YouTube / Vimeo)**:
   - Sluggish initial loading (+1.5s to +3s overhead per player).
   - Cluttered third-party UI, tracking cookies, and branding.
   - Restricted CSS styling and lack of custom control integration.
2. **Paid External Video CDNs (Mux, Cloudflare Stream, BunnyCDN)**:
   - Recurring monthly expenses and bandwidth caps.
   - Complex API keys and authentication handshakes.

**The Solution**: Darshan Naidu's portfolio uses a **100% free, self-hosted video streaming architecture** running natively on **Vercel's global Edge CDN** via HTTP 206 Range requests and an edge Service Worker cache.

---

## 2. The FastStart Atom Principle

An MP4 container (ISO Base Media format) consists of various data chunks known as **atoms** or **boxes**:
- **`mdat` (Media Data)**: Contains the raw compressed video frames and audio samples (typically 95%+ of the file size).
- **`moov` (Movie Metadata)**: Contains the index, timeline, codec profile, duration, and frame offset references required by the browser to decode and seek the media.

### Default Video Export vs. Web-Optimized Export

```
Standard Export (Slow Initial Web Playback):
┌─────────────────────────────────────────────────────────────┬──────────┐
│                     `mdat` (Media Data)                     │  `moov`  │
│                       [Megabytes...]                        │ (Header) │
└─────────────────────────────────────────────────────────────┴──────────┘
 Browsers must download almost the ENTIRE file before finding the index!

Web-Optimized FastStart (Instant Web Playback):
┌──────────┬─────────────────────────────────────────────────────────────┐
│  `moov`  │                     `mdat` (Media Data)                     │
│ (Header) │                       [Megabytes...]                        │
└──────────┴─────────────────────────────────────────────────────────────┘
 Browser reads the header on the first 32 KB chunk and starts playing immediately!
```

When `moov` is placed at the front of the file:
1. The browser initiates an HTTP `Range: bytes=0-` request.
2. The browser immediately receives the `moov` atom in the first 32 KB–64 KB slice.
3. The video engine begins hardware decoding and renders the first frame within **150ms–250ms**.

### How to Verify FastStart on macOS

Run the following command to check the hex structure of an MP4:

```bash
# Check the first 64 bytes of the video file
xxd -l 64 assets/videos/reels-12.mp4
```

If you see `moov` within the first 64 bytes, FastStart is enabled:
```
00000000: 0000 0020 6674 7970 6973 6f6d ...  ... ftypisom
00000010: 0000 0001 6973 6f6d 6176 6331 ...  ... isomavc1
00000020: 0001 b5c2 6d6f 6f76 0000 006c ...  ... ..moov...
```

---

## 3. Zero-Black-Box Poster Strategy

When a `<video>` element mounts in the DOM, there is a natural delay while the browser initializes the media pipeline. Without careful styling, browsers render an unsightly **black box**.

To eliminate this completely:
1. **Dual Poster Binding**:
   - Every video card has a companion WebP poster image (compressed to ~25 KB).
   - The card element has a `.reels-poster` background image set in CSS.
   - The `<video>` element itself specifies the `poster` attribute.
2. **Immediate Visual Continuity**:
   - The user sees a high-res, full-fidelity frame instantly (0ms layout shift).
   - When the video decodes and starts playing, it seamlessly crossfades over the identical poster.

---

## 4. Native Frame Extraction (No ffmpeg Needed)

While tools like `ffmpeg` are standard for video processing, developer and CI environments often lack `ffmpeg` installed by default. This repository uses a native macOS Swift script using `AVFoundation` to extract pristine keyframes without any third-party dependencies.

### Native Swift Keyframe Extractor

Save and run this script using `swift -`:

```swift
import AVFoundation
import AppKit

let videoPath = "assets/videos/reels-12.mp4"
let outputPath = "assets/videos/reels-12-poster.png"

let url = URL(fileURLWithPath: videoPath)
let asset = AVAsset(url: url)
let generator = AVAssetImageGenerator(asset: asset)
generator.appliesPreferredTrackTransform = true
generator.requestedTimeToleranceBefore = .zero
generator.requestedTimeToleranceAfter = .zero

let time = CMTime(seconds: 0.1, preferredTimescale: 600)
do {
    let cgImage = try generator.copyCGImage(at: time, actualTime: nil)
    let bitmapRep = NSBitmapImageRep(cgImage: cgImage)
    let pngData = bitmapRep.representation(using: .png, properties: [:])!
    try pngData.write(to: URL(fileURLWithPath: outputPath))
    print("Frame extracted to \(outputPath)")
} catch {
    print("Failed: \(error)")
}
```

### WebP Compression via Python Pillow

To convert the extracted PNG to an ultra-efficient 85% quality WebP:

```python
from PIL import Image

im = Image.open("assets/videos/reels-12-poster.png")
im.save("assets/videos/reels-12-poster.webp", "WEBP", quality=85)
```

This reduces a 1.2 MB uncompressed frame to **~25 KB–30 KB** with zero noticeable visual loss.

---

## 5. HTTP 206 Partial Content & Edge Range Requests

Modern browsers stream media via **HTTP 206 Partial Content**. Instead of requesting an entire 8 MB file in a single GET request, the browser requests byte chunks:

```http
GET /assets/videos/reels-12.mp4 HTTP/2
Host: darshannaidu.vercel.app
Range: bytes=0-1048575
```

Vercel's Edge CDN responds:
```http
HTTP/2 206 Partial Content
Content-Range: bytes 0-1048575/3519747
Content-Length: 1048576
Content-Type: video/mp4
Accept-Ranges: bytes
```

### The Service Worker Multiplier (`sw.js`)

Our custom Service Worker intercepts these Range requests:
1. It caches the initial `0-1048575` byte slice in `CacheStorage`.
2. When the user hovers, re-visits the page, or loops the video, the initial slice is served from memory with **0ms latency**.
3. The remaining video bytes stream smoothly in the background as playback continues.

---

## 6. Why `<link rel="preload" as="video">` is Forbidden

It is tempting to put `<link rel="preload" as="video" href="...">` in the HTML `<head>`, but this is a critical mistake in modern Chromium and Safari:

> [!WARNING]
> When a browser encounters `<link rel="preload" as="video">`, it dispatches an unrestricted standard `GET` request downloading the **ENTIRE video file**.
> When the `<video>` element on the page mounts, it simultaneously dispatches an **HTTP 206 Range request**.
> This causes the browser to download the exact same video **twice** over the network, doubling bandwidth consumption and causing mobile network congestion.

**The Golden Rule**: Never preload videos with `<link rel="preload">`. Rely exclusively on `<video preload="auto" loop muted playsinline>` and speculative pre-warming via `fast-loader.js`.

---

## 7. Step-by-Step: Adding a New Reel to the Archive

Follow this exact checklist when adding a new reel to the portfolio:

### Step 1: Encode to Web-Optimized H.264 FastStart

Use macOS `avconvert` or `ffmpeg`:

```bash
# macOS native command
avconvert -p PresetMediumQuality -i source_video.mp4 -o assets/videos/reels-14.mp4

# OR with ffmpeg (if installed)
ffmpeg -i source_video.mp4 -c:v libx264 -crf 23 -preset slow -movflags +faststart -c:a aac -b:a 128k assets/videos/reels-14.mp4
```

### Step 2: Generate WebP Poster

Extract keyframe at 0.1s and save as `assets/videos/reels-14-poster.webp`.

### Step 3: Mirror Assets to `dist/`

Every production file in `assets/videos/` must be mirrored to `dist/assets/videos/`:

```bash
cp assets/videos/reels-14.mp4 dist/assets/videos/
cp assets/videos/reels-14-poster.webp dist/assets/videos/
```

### Step 4: Register in `assets/index-CnbWzhzO.js`

Add the card entry to the reels array in `assets/index-CnbWzhzO.js` (and mirror to `dist/assets/index-CnbWzhzO.js`):

```javascript
{
  src: "/assets/videos/reels-14.mp4",
  poster: "/assets/videos/reels-14-poster.webp",
  aspect: "9/16", // or "16/9" for widescreen
  title: "Project Title",
  category: "Commercial Motion"
}
```

### Step 5: Verify Locally

Start the local server and verify playback:

```bash
python3 server.py
# Open http://localhost:8088/video-archive in your browser
```

---

## 8. Current Video Catalog & Sequence Rules

The Video Archive follows a strict visual sequence designed to balance vertical reels with widescreen hero features:

| Position | Video File | Poster File | Aspect Ratio | Format & Pacing |
| :--- | :--- | :--- | :--- | :--- |
| **Top Hero** | `x-entiall.mp4` | `reels-1-poster.webp` | 16:9 Widescreen | Flagship commercial campaign |
| **Card 1** | `reels-2.mp4` | `reels-2-poster.webp` | 9:16 Vertical | High-energy urban lifestyle |
| **Card 2** | `reels-3.mp4` | `reels-3-poster.webp` | 9:16 Vertical | Fast-paced product & kinetic edit |
| **Card 3** | `reels-4.mp4` | `reels-4-poster.webp` | 9:16 Vertical | Sound-design synchronized narrative |
| **Card 4** | `reels-7.mp4` | `reels-7-poster.webp` | 16:9 Widescreen | Cinematic widescreen visual study |
| **Card 5** | `reels-6.mp4` | `reels-6-poster.webp` | 16:9 Widescreen | Studio motion & lighting showcase |
| **Card 6** | `reels-8.mp4` | `reels-8-poster.webp` | 9:16 Vertical | Social retention edit with graphic hooks |
| **Card 7** | `reels-9.mp4` | `reels-9-poster.webp` | 9:16 Vertical | Color grading & micro-cut exercise |
| **Card 8** | `reels-10.mp4` | `reels-10-poster.webp` | 9:16 Vertical | Commercial reel with rapid typography |
| **Card 9** | `reels-11.mp4` | `reels-11-poster.webp` | 9:16 Vertical | Atmospheric sound design & visual flow |
| **Card 10** | `reels-12.mp4` | `reels-12-poster.webp` | 9:16 Vertical | Kinetic street lifestyle & rapid pacing |
| **Card 11** | `reels-13.mp4` | `reels-13-poster.webp` | 9:16 Vertical | Motion design & dynamic narrative cut |
| **Card 12** | `reels-5.mp4` | `reels-5-poster.webp` | 16:9 Featured | Full-bleed widescreen feature cut |
| **Card 13** | `x-entiall.mp4` | `reels-1-poster.webp` | 16:9 Featured | Closing flagship showcase cut |

> [!IMPORTANT]
> **Cardinal Rule**: Never place `x-entiall.mp4` as Card #1 immediately below the top hero banner. Card #1 must always be `reels-2.mp4` to prevent duplicate video rendering at the top of the archive.
