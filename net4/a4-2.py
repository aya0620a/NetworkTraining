from flask import Flask, make_response, render_template, session, request

app = Flask(__name__)
app.secret_key = "abc"
# セッション変数を利用するためには秘密鍵(secret_key)の登録が必要

message = "セッション変数を利用します。"

@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def input():
    if "count" in session:
        # "count"という名前のセッション変数を探す．
        count = session["count"]
        # あれば変数countに代入する
    else:
        # なければ変数countを0に初期化する．
        count = 0
        
    #inputタグのnameがxの値を取得
    y = request.args.get("y")
    if y is not None:
        count = int(y)
        session["count"] = count
        
    message = "f(x) = " + str(count)
        
    return render_template("a4-2.html", title="セッションの利用", message=message, count=count)
    # a4-2.htmlを表示する．

#加算、減算、乗算、除算のボタンを押されたときの処理
@app.route("/", methods=["POST"])

def calc():
    y = request.form.get('y', type=int)  # 'y'というキーが存在しない場合はNoneを返す
    # inputタグのname属性が"y"のときの値を取得する．
    
    if y is None:
        y = 1  # yがNoneの場合、デフォルト値として1を設定
    
    if "count" in session:
        # "count"という名前のセッション変数を探す．
        count = session["count"]
        # あれば変数countに代入する
    else:
        # なければ変数countを0に初期化する．
        count = 0
        
    # inputタグのname属性が"add"のときの処理
    if "add" in request.form:
        count += y
    # inputタグのname属性が"sub"のときの処理
    elif "sub" in request.form:
        count -= y
    # inputタグのname属性が"mul"のときの処理
    elif "mul" in request.form:
        count *= y
    # inputタグのname属性が"div"のときの処理
    elif "div" in request.form:
        count /= y
        
    session["count"] = count
        
    message = "f(x) = " + str(count)
            
    response = make_response(render_template("a4-2.html", title="セッションの利用", message=message, count=count))
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")