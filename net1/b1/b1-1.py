from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

with open("b1-1.html", mode="r", encoding="utf-8") as file:
    input = file.read()
    # 入力フォームとなるHTMLファイルを読み込み，inputに代入する．


position = ["過去のイベント", "過去のイベント", "未来のイベント"]
name = ["高校卒業", "大学入学", "大学卒業"]
time = ["2021/3/9", "2021/4/1", "2026/3/31"]
place = ["高校", "大学", "大学"]
color = ["black", "black", "red"]


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        _url = urlparse(self.path)
        query = parse_qs(_url.query)
        # URLからクエリパラメータを取り出す．

        if "id" in query:
            id = int(query["id"][0])
            # idの値を取り出す．
            if 1 <= id <= 3:
                html = input.format(title=position[id - 1], message=name[id - 1] + ": 日付: " + time[id - 1], color=color[id - 1])
                self.wfile.write(html.encode("utf-8"))
            else:
                self.send_error(400, "idの値が不正です")
                # idの値の範囲が1以上3以下でない場合は，そのことを示すメッセージを表示する．
        else:
            self.send_error(400, "idが指定されていません")
            # idが指定されていない場合は，そのことを示すメッセージを表示する．

        return
    
HTTPServer(("", 8000), MyServerHandler).serve_forever()