
# https://docs.python.org/3/library/http.server.html
# https://www.digitalocean.com/community/tutorials/python-simplehttpserver-http-server

# lists the files & contents on the default dir

# python -m http.server 8000
# python -m http.server --bind 127.0.0.1
# python -m http.server --directory /tmp/

# http://localhost:8000/

from http import server, HTTPStatus, HTTPMethod
import socketserver

PORT = 8000

# Handler = server.SimpleHTTPRequestHandler
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

class HttpHandler(server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, directory="/Users/mac/GoogleDrive/")

    # def handle_one_request(self):
    #     print(self.client_address[0])
    #     return super().handle_one_request()

    # def do_GET(self):
    #     self.send_response(HTTPStatus.OK)
    #     self.end_headers()
    #     self.wfile.write(b'Hello world')
    # def do_POST(self):
    #     content_length = int(self.headers['Content-Length'])
    #     body = self.rfile.read(content_length)
    #     self.send_response(HTTPStatus.OK)
    #     self.end_headers()
    #     self.wfile.write(b'Hello world')

httpd = socketserver.TCPServer(("", PORT), HttpHandler)

while True:
    print("serving at port", PORT)
    httpd.handle_request()