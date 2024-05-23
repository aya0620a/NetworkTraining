from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

schema = ["イベント名", "日付", "場所", "残り日数"]

table = [
    ["高校卒業", "2021/3/9", "高校"],
    ["大学入学", "2021/4/1", "大学"],
    ["大学卒業", "2026/3/31", "大学"],
]


#コンテキストプロセッサの定義
@app.context_processor
#登録用プロセッサとしてget_remaining_daysを定義
def remaining_days_processor():
    def get_remaining_days(date_str):
        event_date = datetime.strptime(date_str, "%Y/%m/%d")
        today = datetime.today()
        remaining_days = (event_date - today).days
        return remaining_days
    #get_remaining_daysをプロセッサとして登録
    return dict(get_remaining_days=get_remaining_days)

@app.route("/")
def render_table():
    return render_template("a3-4.html", title="A3-4", schema=schema, table=table)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")