import datetime
from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("sample1-3.html", mode="r", encoding="utf-8") as file:
    input = file.read()
    # 入力フォームとなるHTMLファイルを読み込み，inputに代入する．
with open("sample1-2.html", mode="r", encoding="utf-8") as file:
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
        name = form["name"].value
        # 入力フォームにある名前(name)のデータを取り出す．
        try:
            age = int(form["age"].value)
            # 入力フォームにある年齢(age)のデータを取り出し，整数化する．

            dt = datetime.datetime.now()
            # 現在の日時を取得する．

            message = "{}さんが生まれたのは{}年か{}年．".format(name, dt.year - age - 1, dt.year - age)
            # 名前と年齢から計算した生まれ年をメッセージにする．
        except ValueError:
            message = "年齢が正しくありません．"
            # 入力フォームにある年齢が正しくない場合は，その旨をメッセージにする．

        self.send_response(200)
        self.end_headers()
        html = output.format(title="出力画面", message=message)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()