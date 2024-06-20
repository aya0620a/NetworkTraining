import datetime

from flask import Flask, render_template

app = Flask(__name__)

schema = ["イベント名", "日付", "場所"]

table = [
    ["高校卒業", "2021/3/9", "高校"],
    ["大学入学", "2021/4/1", "大学"],
    ["大学卒業", "2026/3/31", "大学"],
]

@app.route("/")
def template():
    dt = datetime.datetime.now()
    message = "Last updated:{a}年{b}月{c}日".format(a=dt.year, b=dt.month, c=dt.day)
    return render_template("a6-1.html", title="イベント情報", message=message, schema=schema, table=table )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")   