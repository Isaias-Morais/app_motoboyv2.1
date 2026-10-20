const CACHE_NAME = "app-motoboy-shell-v2";
const APP_SHELL = [
  "./",
  "index.html",
  "login.html",
  "cadastro.html",
  "criar-moto.html",
  "registrar.html",
  "gastos.html",
  "relatorio.html",
  "minha-moto.html",
  "offline.html",
  "manifest.webmanifest",
  "css/style.css",
  "js/app.js",
  "img/logo-icon.png",
  "img/pwa-icon.svg",
  "img/pwa-icon-maskable.svg"
];

self.addEventListener("install", event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(APP_SHELL)));
  self.skipWaiting();
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
    ))
  );
  self.clients.claim();
});

self.addEventListener("fetch", event => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.method !== "GET" || url.origin !== self.location.origin) {
    return;
  }

  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then(response => {
          const copy = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request).then(cached => cached || caches.match("offline.html")))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then(cached => cached || fetch(request))
  );
});
