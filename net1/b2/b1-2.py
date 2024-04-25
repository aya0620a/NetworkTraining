from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
from dateutil.relativedelta import relativedelta
import calendar


with open("b1-2.html", mode="r", encoding="utf-8") as file:
    input = file.read()
    # 入力フォームとなるHTMLファイルを読み込み，inputに代入する．


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = input.format(title="入力画面" , message="イベント名と日付を入力してください")
        self.wfile.write(html.encode("utf-8"))
        # 入力フォームを表示する．
        return
    
    def do_POST(self):
        form = FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})
        name = form["name"].value
        
        try: 
            date = datetime.datetime.strptime(form["date"].value, "%Y-%m-%d")            
            # dateの値を取り出す．
            dt = datetime.datetime.now()
            
            diff = date - dt
            
            
            message = "{}まで、あと{}日です。".format(name, (diff.days + 1))
            # メッセージを作成する．
        
        except ValueError:
            self.send_error(400, "日数が整数でありません")
            # 日数が整数でない場合は，そのことを示すメッセージを表示する．
            
        self.send_response(200)
        self.end_headers()
        html = input.format(title="入力画面", message=message)
        self.wfile.write(html.encode("utf-8"))

        return
        
        
    
HTTPServer(("", 8000), MyServerHandler).serve_forever()