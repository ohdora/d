from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()

#!/usr/bin/env python3

print("Content-type: text/html")
print()
print("<h1>Hello, Daria!</h1>")
