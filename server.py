from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import imageHandler

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        newUrl = imageHandler.handleImage
        response.body = { "url" : newUrl}
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("listening on port " + str(PORT))
httpd.serve_forever()