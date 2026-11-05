/**
 * Darshan Naidu Portfolio - Fast Loader & Video Stream Engine
 * High-performance edge cache pre-warming, speculative link prefetch, and range buffer manager.
 */
(function() {
  'use strict';

  // 1. Service Worker Registration
  if ('serviceWorker' in navigator && window.location.protocol.startsWith('http')) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/sw.js', { scope: '/' }).catch(function() {});
    });
  }

  // 2. Speculative Navigation Prefetch (Hover & Touch Pre-warming)
  const prefetchedUrls = new Set();
  function prefetchUrl(url) {
    if (!url || prefetchedUrls.has(url)) return;
    try {
      const parsed = new URL(url, window.location.origin);
      if (parsed.origin !== window.location.origin) return;
      prefetchedUrls.add(url);

      const link = document.createElement('link');
      link.rel = 'prefetch';
      link.href = url;
      link.as = 'document';
      document.head.appendChild(link);
    } catch (e) {}
  }

  let hoverTimeout = null;
  document.addEventListener('mouseover', function(e) {
    const a = e.target.closest('a');
    if (!a || !a.href) return;
    hoverTimeout = setTimeout(function() {
      prefetchUrl(a.href);
    }, 65);
  }, { passive: true });

  document.addEventListener('mouseout', function(e) {
    if (hoverTimeout) {
      clearTimeout(hoverTimeout);
      hoverTimeout = null;
    }
  }, { passive: true });

  document.addEventListener('touchstart', function(e) {
    const a = e.target.closest('a');
    if (a && a.href) prefetchUrl(a.href);
  }, { passive: true });

  // 3. Background Video Pre-warming (Warm Vercel Edge & Local Cache)
  function prewarmVideos() {
    const isVideoArchive = window.location.pathname.includes('video-archive');
    const targetVideos = isVideoArchive
      ? ['/assets/videos/reels-1.mp4', '/assets/videos/reels-2.mp4', '/assets/videos/reels-3.mp4']
      : ['/assets/videos/x-entiall.mp4', '/assets/videos/reels-1.mp4'];

    targetVideos.forEach(function(videoUrl, idx) {
      setTimeout(function() {
        fetch(videoUrl, {
          headers: { 'Range': 'bytes=0-262143' },
          mode: 'cors',
          credentials: 'omit'
        }).catch(function() {});
      }, 1000 + (idx * 400));
    });
  }

  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(prewarmVideos);
  } else {
    setTimeout(prewarmVideos, 1500);
  }
})();
