#!/usr/bin/env python3

import http.server

class Server(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"name": "John", "age": 30, "city": "New York"}')
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "OK"}')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "FAIL", "message": "Endpoint not found"}')

if __name__ == "__main__":
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, Server)
    print("Starting server on port 8000...")
    httpd.serve_forever()
