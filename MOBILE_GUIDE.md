# Mobile & Responsive Design System

> **Responsive Engineering Guide**: A complete breakdown of viewport adaptation, mobile framing fixes, typography fluid clamps, and zero-overflow guarantees across **Darshan Naidu's Portfolio**.

---

## 📑 Table of Contents

1. [Responsive Philosophy](#1-responsive-philosophy)
2. [Viewport Breakpoints & Grid Matrix](#2-viewport-breakpoints--grid-matrix)
3. [The Out-of-Frame Bugs & Solutions](#3-the-out-of-frame-bugs--solutions)
   - [Bug 1: Hero Thumbnail Aspect-Ratio & 90svh Crop](#bug-1-hero-thumbnail-aspect-ratio--90svh-crop)
   - [Bug 2: Rigid Title Overflow & Fluid Typography Clamp](#bug-2-rigid-title-overflow--fluid-typography-clamp)
   - [Bug 3: Metadata Misalignment & 2x2 Grid System](#bug-3-metadata-misalignment--2x2-grid-system)
   - [Bug 4: Gallery Grid Collapse & Centered Vertical Reels](#bug-4-gallery-grid-collapse--centered-vertical-reels)
   - [Bug 5: Mobile Button Hitboxes & Overflow Prevention](#bug-5-mobile-button-hitboxes--overflow-prevention)
4. [Zero Horizontal Overflow Guarantee](#4-zero-horizontal-overflow-guarantee)
5. [Automated Mobile Verification Protocol](#5-automated-mobile-verification-protocol)

---

## 1. Responsive Philosophy

Brutalist typography, expansive widescreen cinematics, and multi-column reel galleries look stunning on 27-inch 4K monitors. However, over 65% of social video traffic arrives via mobile smartphones (Instagram bio links, WhatsApp shares, direct links).

The core responsive objective is **uncompromised visual fidelity**:
- Never allow a 16:9 widescreen video to be blindly cropped by vertical screen heights.
- Never allow kinetic typography to spill off the screen edges.
- Ensure all video controls and interactive buttons have generous touch targets.
- Guarantee that `scrollWidth === clientWidth` on every device (zero horizontal jitter).

---

## 2. Viewport Breakpoints & Grid Matrix

| Device Class | Viewport Range | Layout Behavior | Typography Strategy |
| :--- | :--- | :--- | :--- |
| **Mobile Phones** | `< 480px` | 1-Column centered stack, 16:9 hero, 9:16 vertical cards (`max-width: 360px`) | `clamp(2rem, 7.5vw, 3.2rem)` |
| **Phablets & Small Tablets** | `480px – 900px` | 1-to-2 Column fluid flow, adapted metadata grid | `clamp(2.5rem, 6vw, 4rem)` |
| **Laptops & Standard Desktop** | `901px – 1440px` | Alternating 3-column (9:16) & 2-column (16:9) gallery grid | Fixed design system (`4.5rem – 6rem`) |
| **Large Screens & Ultrawide** | `> 1440px` | Max-contained container (`1600px`), centered visual margins | Proportional fluid scaling |

---

## 3. The Out-of-Frame Bugs & Solutions

### Bug 1: Hero Thumbnail Aspect-Ratio & 90svh Crop

#### The Problem
In earlier iterations, the hero banner container had a height rule:
```css
/* Defective rule */
.hero-image-inner {
  height: 90svh;
  width: 100%;
}
```
On an iPhone (390px wide by 844px high), a 90svh height forced the container to be ~760px tall. Because the video inside was a widescreen 16:9 ratio with `object-fit: cover`, the browser was forced to scale the width to ~1350px, **cropping more than 70% of the video horizontally**. The viewer only saw the zoomed-in center of the video.

#### The Fix
Under `@media (max-width: 900px)`, the height rule is overridden and locked strictly to a widescreen 16:9 aspect ratio:

```css
@media (max-width: 900px) {
  .project-hero-image .hero-image-inner {
    aspect-ratio: 16 / 9 !important;
    height: auto !important;
    min-height: 0 !important;
    max-height: none !important;
    width: 100% !important;
  }
}
```
**Result**: The video displays in pristine 16:9 widescreen format, perfectly framed between screen margins with 0% cropping.

---

### Bug 2: Rigid Title Overflow & Fluid Typography Clamp

#### The Problem
Project title headings (`.project-main-title`) used rigid font units like `font-size: 5rem;` or `font-size: 80px;`. On a 390px screen, the text string `"Video Archive"` exceeded 480px in width, pushing the layout off-screen and creating an ugly horizontal scrollbar.

#### The Fix
Implemented CSS `clamp()` combined with `word-break: break-word`:

```css
@media (max-width: 900px) {
  .project-main-title {
    font-size: clamp(2rem, 7.5vw, 3.2rem) !important;
    line-height: 1.05 !important;
    word-break: break-word !important;
    max-width: 100% !important;
  }

  .project-number-wrapper {
    font-size: clamp(1.2rem, 4vw, 1.8rem) !important;
  }
}
```
**Result**: Text dynamically fluid-scales to fit any screen from a 320px iPhone SE to a 430px iPhone 16 Pro Max without hyphenation breaks or clipping.

---

### Bug 3: Metadata Misalignment & 2x2 Grid System

#### The Problem
The project metadata row (Category, Role, Location, Year) was arranged in desktop horizontal flex containers:
```
Desktop:
[(Category) Video Editing · Short-form] [(Role) Sound Design] | [(Location) Vizag] [(Year) 24-26]
```
On mobile, the horizontal text wrapped unpredictably, resulting in misaligned labels, overlapping text spans, and jagged vertical spacing.

#### The Fix
On mobile viewports, the metadata transforms into a disciplined **2x2 clean grid**:

```css
@media (max-width: 900px) {
  .project-metadata {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 1.25rem 1rem !important;
    width: 100% !important;
    padding: 1.5rem 0 !important;
  }

  .metadata-item {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.25rem !important;
  }
}
```
**Result**:
- Row 1: **(Category)** | **(Year)**
- Row 2: **(Role)** | **(Location: Vizag)**

---

### Bug 4: Gallery Grid Collapse & Centered Vertical Reels

#### The Problem
On desktop, the 13-reel gallery features a 3-column / 2-column alternating cadence. On mobile, multi-column layouts made vertical 9:16 reels impossibly narrow (~110px wide), rendering text and micro-cuts unrecognizable.

#### The Fix
The gallery transitions into a **single-column vertical feed**:

```css
@media (max-width: 900px) {
  .reels-gallery {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    gap: 2rem !important;
    width: 100% !important;
  }

  .reels-card {
    width: 100% !important;
    max-width: 360px !important;
    margin: 0 auto !important;
  }

  .reels-card.is-vertical {
    aspect-ratio: 9 / 16 !important;
  }

  .reels-card.is-widescreen,
  .reels-card.is-featured-16-9 {
    aspect-ratio: 16 / 9 !important;
  }
}
```
**Result**: Vertical reels mimic the native Instagram/TikTok mobile viewing experience with generous dimensions (`360px` max width), giving full visual power to Darshan's edits.

---

### Bug 5: Mobile Button Hitboxes & Overflow Prevention

#### The Problem
The custom play/pause/mute control buttons on reel cards were calibrated for mouse pointers (small 24px circles). On touch screens, fingers frequently missed the button or accidentally triggered page navigation. Furthermore, the bottom Instagram banner button had padding that pushed it past screen width.

#### The Fix
- Upgraded button hitboxes to **36px–40px** with generous touch padding.
- Constrained the Instagram banner CTA:
  ```css
  @media (max-width: 900px) {
    .project-ig-banner a {
      width: calc(100% - 2rem) !important;
      max-width: 360px !important;
      margin: 0 auto !important;
      box-sizing: border-box !important;
    }
  }
  ```

---

## 4. Zero Horizontal Overflow Guarantee

Any webpage where `document.documentElement.scrollWidth > window.innerWidth` creates accidental side-swiping and jittery horizontal drift on iOS Safari.

This portfolio enforces a global overflow containment protocol:

```css
html, body {
  width: 100%;
  max-width: 100vw;
  overflow-x: hidden;
  position: relative;
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: border-box;
}
```

---

## 5. Automated Mobile Verification Protocol

To verify that mobile framing remains flawless on future updates, an automated headless Chrome test runs with device emulation:

```javascript
// Emulate iPhone dimensions (390 x 844, DPR: 3, Mobile: true)
await send('Emulation.setDeviceMetricsOverride', {
  width: 390,
  height: 844,
  deviceScaleFactor: 3,
  mobile: true
});

await send('Page.navigate', { url: 'http://localhost:8088/video-archive' });

// Evaluate layout geometry
const check = await send('Runtime.evaluate', {
  expression: `(() => {
    return {
      docWidth: document.documentElement.scrollWidth,
      viewWidth: window.innerWidth,
      hasOverflow: document.documentElement.scrollWidth > window.innerWidth,
      heroRatio: (() => {
        const r = document.querySelector('.project-hero-image .hero-image-inner').getBoundingClientRect();
        return (r.width / r.height).toFixed(3);
      })()
    };
  })()`,
  returnByValue: true
});

console.log(check.result.value);
// Expected: { docWidth: 390, viewWidth: 390, hasOverflow: false, heroRatio: "1.778" }
```
- `hasOverflow: false` confirms zero horizontal drift.
- `heroRatio: "1.778"` confirms exact 16:9 widescreen geometry.
