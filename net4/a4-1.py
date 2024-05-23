from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def input():
    id = request.cookies.get("id")
    # cookieからidデータを取得する．
    if id is None:
        id = ""
    # idがない場合は空文字列を代入する．
    
    return render_template("a4-1in.html", title="フォームの利用", id=id)



@app.route("/", methods=["POST"])
# POSTメソッドでのアクセスは以下が実行される．

def set_cookie():
    # フォームからidデータを取得する．
    id = request.form["id"]
    
    # 2分間有効なcookieをセットする．
    max_age = 60 * 2
    
    if id == '1':
        message = 'イベント名:高校卒業 日程:2021/3/9 場所: 高校'
    elif id == '2':
        message = 'イベント名:大学入学 日程:2021/4/1 場所: 大学'
    elif id == '3':
        message = 'イベント名:大学卒業 日程:2026/3/31 場所: 大学'
    else:
        message = 'idが不正です。'
            
    response = make_response(render_template("a4-1out.html", title="クッキーの利用", message=message, id=id))
    response.set_cookie("id", id, max_age=max_age)
    
    return response

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
        
    return render_template("a4-1out.html", title="イベント情報", message=message, id=id)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")