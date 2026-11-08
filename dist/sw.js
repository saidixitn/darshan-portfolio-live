const CACHE_NAME = 'darshan-portfolio-v9';
const PRECACHE_ASSETS = [
  '/',
  '/video-archive',
  '/works',
  '/assets/index-ZSMau8ex.css',
  '/assets/index-CnbWzhzO.js',
  '/assets/Satoshi-Variable-ChAXbpFa.ttf',
  '/assets/videos/reels-1-poster.webp',
  '/assets/videos/reels-2-poster.webp'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(PRECACHE_ASSETS).catch(err => {
        console.warn('[SW] Precache skipped optional asset:', err);
      });
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  const url = new URL(request.url);

  if (request.method !== 'GET') return;
  if (url.origin !== self.location.origin && !url.origin.includes('fonts.gstatic.com')) return;

  // Handle Range Requests for videos from cache
  if (request.headers.has('range')) {
    event.respondWith(
      (async () => {
        try {
          const cache = await caches.open(CACHE_NAME);
          const cachedResponse = await cache.match(url.pathname);
          if (cachedResponse) {
            const arrayBuffer = await cachedResponse.arrayBuffer();
            const rangeHeader = request.headers.get('range');
            const matches = rangeHeader.match(/bytes=(\d+)-(\d+)?/);
            if (matches) {
              const total = arrayBuffer.byteLength;
              const start = parseInt(matches[1], 10);
              const end = matches[2] ? parseInt(matches[2], 10) : total - 1;
              const chunk = arrayBuffer.slice(start, end + 1);
              return new Response(chunk, {
                status: 206,
                statusText: 'Partial Content',
                headers: [
                  ['Content-Range', `bytes ${start}-${end}/${total}`],
                  ['Accept-Ranges', 'bytes'],
                  ['Content-Length', String(chunk.byteLength)],
                  ['Content-Type', cachedResponse.headers.get('Content-Type') || 'video/mp4'],
                  ['Cache-Control', 'public, max-age=31536000, immutable']
                ]
              });
            }
          }
        } catch (e) {
          // Fall through to network
        }
        return fetch(request);
      })()
    );
    return;
  }

  // Cache-first for immutable static assets
  if (
    url.pathname.startsWith('/assets/') ||
    url.pathname.endsWith('.webp') ||
    url.pathname.endsWith('.ttf') ||
    url.pathname.endsWith('.woff2') ||
    url.pathname.endsWith('.css') ||
    url.pathname.endsWith('.js')
  ) {
    event.respondWith(
      caches.match(request).then(cached => {
        if (cached) return cached;
        return fetch(request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then(c => c.put(request, clone));
          }
          return networkResponse;
        });
      })
    );
    return;
  }

  // Stale-while-revalidate for HTML pages
  event.respondWith(
    caches.match(request).then(cached => {
      const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse && networkResponse.status === 200) {
          const clone = networkResponse.clone();
          caches.open(CACHE_NAME).then(c => c.put(request, clone));
        }
        return networkResponse;
      }).catch(() => cached);
      return cached || fetchPromise;
    })
  );
});
