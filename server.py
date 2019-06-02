from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import imageHandler
import json

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        url = json.loads(body.decode())['url']
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(str.encode(imageHandler.handleImage(url)))
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("listening on port " + str(PORT))
httpd.serve_forever()