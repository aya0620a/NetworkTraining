from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

schema = ["イベント名", "日付", "場所", "残り日数"]

def daycount(date_str):
    event_date = datetime.strptime(date_str, "%Y/%m/%d")
    today = datetime.today()
    if event_date < today:
        remaining_days = (-1) * (today-event_date).days
    else:
        remaining_days = (event_date - today).days
    return remaining_days

@app.context_processor
def utility_processor():
    return dict(daycount=daycount)

@app.route("/")
def render_table():
    table = [
        ["高校卒業", "2021/3/9", "高校"],
        ["大学入学", "2021/4/1", "大学"],
        ["大学卒業", "2026/3/31", "大学"],
    ]
    return render_template("a3-4.html", title="A3-4", schema=schema, table=table)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")