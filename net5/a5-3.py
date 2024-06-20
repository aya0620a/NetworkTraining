import sqlite3
import datetime

# sqlite用モジュールのインポート
from flask import Flask, g, render_template, request, redirect

# グローバル変数gのインポート


app = Flask(__name__)

#現在時間を"yyyy-mm-dd"の形式で取得
now = datetime.datetime.now().strftime("%Y-%m-%d")

def get_db():
    if "db" not in g:
        # gはリクエストごとに用意されるFlaskのオブジェクト
        # gに"db"が含まれていない場合にデータベースへの接続が行われる．
        g.db = sqlite3.connect("a5-2.db")
        # データベースへの接続
    return g.db


def close_db():
    db = g.pop("db", None)
    # gから"db"を取り出す．
    if db is not None:
        # gに"db"が含まれていた場合にはデータベースとの接続を終了する．
        db.close()
        # データベースの接続終了
        
#フォームからのデータを受け取る
@app.route("/post", methods=["POST"])
def post():
    db = get_db()
    cursor = db.cursor()
    event_name = request.form["name"]
    event_date = request.form["date"]
    event_place = request.form["place"]

    cursor.execute("INSERT INTO events (event_name, event_date, event_place) VALUES (?, ?, ?)", (event_name, event_date, event_place))
    db.commit()
    return redirect("/")




@app.route("/", methods=["GET"])
def database():
    db = get_db()
    # データベースへの接続
    cursor = db.cursor()
    cursor.execute("SELECT * FROM events")
    table_all = cursor.fetchall()
    cursor.execute("SELECT * FROM events WHERE event_name LIKE '%フェスティバル%'")
    table_festival = cursor.fetchall()
    cursor.execute("SELECT * FROM events WHERE event_date > CURRENT_DATE")
    table_future = cursor.fetchall()
    cursor.execute("SELECT * FROM events WHERE event_name LIKE '%マラソン%' AND event_date < CURRENT_DATE")
    table_original = cursor.fetchall()
    schema = ["ID", "イベント名", "日程", "場所"]
    

    return render_template(
        "a5-3.html",
        title="DBテスト",
        schema=schema,
        table_all=table_all,
        table_festival=table_festival,
        table_future=table_future,
        table_original=table_original,
        now=now
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")