import http.server
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0].split('#')[0]
        if path.rstrip('/') == '/admin':
            self.path = '/admin.html'
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8090))
    server = http.server.HTTPServer(('0.0.0.0', port), Handler)
    print(f'Serving on http://localhost:{port}')
    server.serve_forever()
