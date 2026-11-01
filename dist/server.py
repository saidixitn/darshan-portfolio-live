#!/usr/bin/env python3
"""
Darshan Naidu Portfolio Server
Run with: python3 server.py
"""

import http.server
import socket
import socketserver
import os
import mimetypes
from pathlib import Path

PORT = int(os.environ.get("PORT", 8088))
ROOT_DIR = Path(__file__).resolve().parent

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("application/javascript", ".mjs")
mimetypes.add_type("image/avif", ".avif")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("font/woff", ".woff")
mimetypes.add_type("font/ttf", ".ttf")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("video/mp4", ".mp4")
mimetypes.add_type("video/mp4", ".MP4")

class DarshanPortfolioHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def translate_path(self, path):
        clean_path = path.split('?', 1)[0].split('#', 1)[0]
        # Strip /test if present so all paths resolve locally
        if clean_path == "/test" or clean_path == "/test/":
            clean_path = "/"
        elif clean_path.startswith("/test/"):
            clean_path = clean_path[5:]

        orig_path = super().translate_path(clean_path)

        if os.path.exists(orig_path):
            if os.path.isdir(orig_path):
                idx = os.path.join(orig_path, "index.html")
                if os.path.exists(idx): return idx
            return orig_path

        if os.path.exists(orig_path + ".html"):
            return orig_path + ".html"

        dir_idx = os.path.join(orig_path, "index.html")
        if os.path.exists(dir_idx):
            return dir_idx

        if orig_path.endswith(os.sep):
            stripped = orig_path[:-1]
            if os.path.exists(stripped + ".html"): return stripped + ".html"
            if os.path.exists(stripped): return stripped

        basename = os.path.basename(orig_path.rstrip(os.sep))
        if "." not in basename:
            root_idx = os.path.join(self.directory, "index.html")
            if os.path.exists(root_idx): return root_idx

        return orig_path

    def guess_type(self, path):
        mime, _ = mimetypes.guess_type(path)
        return mime or super().guess_type(path)

class RobustServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
    request_queue_size = 128

    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            try:
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except OSError:
                pass
        super().server_bind()

if __name__ == "__main__":
    os.chdir(ROOT_DIR)
    handler = lambda *args, **kwargs: DarshanPortfolioHandler(*args, directory=str(ROOT_DIR), **kwargs)
    port = PORT
    for attempt_port in [port, 8088, 8080, 8000, 3000, 5000]:
        try:
            httpd = RobustServer(("", attempt_port), handler)
            print(f"🚀 Darshan Portfolio serving at http://localhost:{attempt_port}")
            httpd.serve_forever()
            break
        except OSError:
            continue
