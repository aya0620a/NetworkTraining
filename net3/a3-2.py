from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def table():
    schema = ["イベント名", "日付", "場所"]
    
    table = [
             ["高校卒業", "2021/3/9", "高校"],
             ["大学入学", "2021/4/1", "大学"],
             ["大学卒業", "2026/3/31", "大学"]
            ]

    return render_template("a3-2.html", title="A3-2", schema=schema, table=table)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
