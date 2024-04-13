from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

with open("sample1-2.html", mode="r", encoding="utf-8") as file:
    template = file.read()

routes = []

def route(path, method):
    routes.append((path, method))

route("/id1", "id1")
route("/id2", "id2")
route("/id3", "id3")

class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)
        for r in routes:
            if r[0] == _url.path:
                eval("self." + r[1] + "()")
                break
        else:
            self.error()

    def id1(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(title="Event Information", message="Event 1: Event A - Date: January 15, 2025")
        self.wfile.write(html.encode("utf-8"))

    def id2(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(title="Event Information", message="Event 2: Event B - Date: March 20, 2026")
        self.wfile.write(html.encode("utf-8"))

    def id3(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(title="Event Information", message="Event 3: Event C - Date: December 5, 2026")
        self.wfile.write(html.encode("utf-8"))

    def error(self):
        self.send_error(404, "Not Found")

HTTPServer(("", 8000), MyServerHandler).serve_forever()
