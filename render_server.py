# Guarda esto como render_server.py
import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor corriendo en el puerto {PORT}")
    httpd.serve_forever()
