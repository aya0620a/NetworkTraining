from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

with open("a1-3.html", mode="r", encoding="utf-8") as file:
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
        html = template.format(title="過去のイベント", message="高校卒業: 日付: January 15, 2025", color="black")
        self.wfile.write(html.encode("utf-8"))

    def id2(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(title="過去のイベント", message="大学入学: 日付: March 20, 2026", color="black")
        self.wfile.write(html.encode("utf-8"))

    def id3(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(title="未来のイベント", message="大学卒業:  日付: December 5, 2026", color="red")
        self.wfile.write(html.encode("utf-8"))

    def error(self):
        self.send_error(404, "Not Found")

HTTPServer(("", 8000), MyServerHandler).serve_forever()
