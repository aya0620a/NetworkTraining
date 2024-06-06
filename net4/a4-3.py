from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def address3a():
    with open("a4-3.txt", encoding="utf-8") as file:
        data = []
        for text in file:
            # ファイルから１行づつ読み出し，textに代入する
            data.append(text.split(","))
            # textを","で分割し，dataに追加する
            
            #先頭の要素の"-"を削除したものをdate_datestrに代入
            date_datestr = data[-1][0].replace("-", "")
            #date_datestrを日付に変換
            date = datetime.datetime.strptime(date_datestr, "%Y%m%d")
            #今日の日付を取得
            today = datetime.datetime.now()
            #イベントの日付が今日以前であればjudgeにTrueを代入
            judge = date <= today          
        
            #dateに"過去のイベント"かどうかを表す真偽値を追加
            data[-1].append(judge)
        
        
    #イベントの情報を格納するリスト
    schema = ["日程", "イベント名", "過去のイベントかどうか"]
        
    return render_template("a4-3.html", title="イベント一覧", schema=schema, table=data)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")