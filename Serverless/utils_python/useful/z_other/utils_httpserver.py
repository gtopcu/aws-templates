
# https://docs.python.org/3/library/http.server.html
# https://www.digitalocean.com/community/tutorials/python-simplehttpserver-http-server

# lists the files & contents on the default dir

# python -m http.server 8000
# python -m http.server --bind 127.0.0.1
# python -m http.server --directory /tmp/

# http://localhost:8000/

import http.server
import socketserver

PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        print(self.client_address[0])
        return super().handle_one_request()

httpd = socketserver.TCPServer(("", PORT), MyHandler)

while True:
    print("serving at port", PORT)
    httpd.handle_request()