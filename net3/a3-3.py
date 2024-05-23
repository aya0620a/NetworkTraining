from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

schema = ["イベント名", "日付", "場所", "残り日数"]

table = [
    ["高校卒業", "2021/3/9", "高校"],
    ["大学入学", "2021/4/1", "大学"],
    ["大学卒業", "2026/3/31", "大学"],
]

@app.template_filter("remaining_days")
def daycount_filter(date_str):
    event_date = datetime.strptime(date_str, "%Y/%m/%d")
    today = datetime.today()
    remaining_days = (event_date - today).days
    
    return remaining_days

#テンプレートフィルタday
app.jinja_env.filters["remaining_days"] = daycount_filter



@app.route("/")
def render_table():
    return render_template("a3-3.html", title="A3-3", schema=schema, table=table)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")