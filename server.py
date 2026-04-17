from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import webbrowser

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    pass

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running: http://localhost:{PORT}")

    webbrowser.open(f"http://localhost:{PORT}/index.html")

    httpd.serve_forever()