from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from kvstore import KeyValueStore

store = KeyValueStore()

class KVStoreHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def _parse_path(self):
        parts = self.path.strip("/").split("/")
        return parts if len(parts) == 2 else (None, None)

    def do_GET(self):
        _, key = self._parse_path()
        success, result = store.read(key)
        self._set_headers(200 if success else 404)
        self.wfile.write(json.dumps({"message": result}).encode())

    def do_POST(self):
        _, key = self._parse_path()
        content_len = int(self.headers["Content-Length"])
        data = json.loads(self.rfile.read(content_len))
        value = data.get("value")
        success, result = store.create(key, value)
        self._set_headers(201 if success else 409)
        self.wfile.write(json.dumps({"message": result}).encode())

    def do_PUT(self):
        _, key = self._parse_path()
        content_len = int(self.headers["Content-Length"])
        data = json.loads(self.rfile.read(content_len))
        value = data.get("value")
        success, result = store.update(key, value)
        self._set_headers(200 if success else 404)
        self.wfile.write(json.dumps({"message": result}).encode())

    def do_DELETE(self):
        _, key = self._parse_path()
        success, result = store.delete(key)
        self._set_headers(200 if success else 404)
        self.wfile.write(json.dumps({"message": result}).encode())

def run(server_class=HTTPServer, handler_class=KVStoreHandler, port=8083):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
