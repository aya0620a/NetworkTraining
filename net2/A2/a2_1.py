from flask import Flask, render_template
# flaskモジュールからFlaskクラスとrender_templateメソッドをインポートする

app = Flask(__name__)
# Flaskインスタンスを生成する．


@app.route("/")
# ルート"/"にアクセスされた場合にsampleが呼び出されることを指定する．メソッドの名前は任意である．
def sample():
    return render_template("a2_1.html")
    # templateフォルダに入っているsample2-1.htmlを表示する．


if __name__ == "__main__":
    # このプログラムが直接起動されたものであれば以下を実行する．
    app.debug = True
    # デバッグ機能をONにする．
    app.run(host="localhost")
    # ホスト名をlocalhostにして，Webアプリケーションを起動する．