
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def input():
    return render_template("a2-4in.html", title="フォームの利用")


@app.route("/", methods=["POST"])
# POSTメソッドでのアクセスは以下が実行される．
def output():
    id = request.form["id"]
    # フォームからidデータを取得する．
    try:
                if id == '1':
                    message = 'イベント名:高校卒業 日程:2021/3/9 場所: 高校'
                elif id == '2':
                    message = 'イベント名:大学入学 日程:2021/4/1 場所: 大学'
                elif id == '3':
                    message = 'イベント名:大学卒業 日程:2026/3/31 場所: 大学'
                else:
                    message = 'idが不正です。'
                    
    except Exception:
        message = "idが正しくありません."
    return render_template("a2-4out.html", title="イベント情報", message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")