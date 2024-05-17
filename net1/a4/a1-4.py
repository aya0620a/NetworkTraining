from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("a1-4in.html", mode="r", encoding="utf-8") as file:
    input = file.read()
    # 入力フォームとなるHTMLファイルを読み込み，inputに代入する．
with open("a1-4out.html", mode="r", encoding="utf-8") as file:
    output = file.read()
    # 出力テンプレートとなるHTMLファイルを読み込み，outputに代入する．


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # GETメソッド（通常）でのアクセスはここで処理する．
        self.send_response(200)
        self.end_headers()
        html = input.format(title="入力画面")
        self.wfile.write(html.encode("utf-8"))
        # 入力フォームを表示する．
        return

    def do_POST(self):
        # POSTメソッドでのアクセスはここで処理する．
        form = FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})
        # 入力フォームの内容を読み込む．
        id = form["id"].value
        # 入力フォームにある名前(name)のデータを取り出す．
        
        # IDに基づいてメッセージを設定する
        if id == '1':
            message = 'イベント名:高校卒業 日程:2021/3/9 場所: 高校'
            color = 'black'
        elif id == '2':
            message = 'イベント名:大学入学 日程:2021/4/1 場所: 大学'
            color = 'black'
        elif id == '3':
            message = 'イベント名:大学卒業 日程:2026/3/31 場所: 大学'
            color = 'red'
        else:
            message = 'idが不正です。'
            color = 'red'
            
        self.send_response(200)
        self.end_headers()
        html = output.format(title="出力画面", message=message, color=color)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()