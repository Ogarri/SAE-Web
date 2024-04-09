import http.server
import socketserver
import os

port = 80
adress = ("", port)

html_files = {
    "/main": "main.html",
    "/bastien": "FFVII.html",
    "/clement": "seraphine.html",
}

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

    def do_GET(self):
        if self.path in html_files:
            self.path = html_files[self.path]
        return super().do_GET()

httpd = socketserver.TCPServer(adress, CustomHandler)

print(f"Server started serving at port {port}")

httpd.serve_forever()
