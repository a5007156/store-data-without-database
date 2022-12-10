import http.server
import json

data = []

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        json_data = json.dumps(data)
        self.wfile.write(json_data.encode())

    def do_POST(self):
        self.send_response(201)
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        request_body_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(request_body_length)
        request_data = json.loads(request_body)
        
        data.append(request_data)
        
        self.wfile.write(json.dumps({}).encode())

httpd = http.server.HTTPServer(('localhost', 8080), RequestHandler)
httpd.serve_forever()
