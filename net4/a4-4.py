from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def filewrite():
    #POSTメソッド
    if request.method == "POST":
        event_name = request.form["event_name"]
        event_date = request.form["event_date"]
        
        with open("a4-3.txt", "a", encoding="utf-8") as file:
            file.write(event_date + "," + event_name + "\n")
        return render_template("a4-4.html", title="ファイルの書き込み", message="書き込み終了")
    
    #GETメソッド
    if request.method == "GET":
        return render_template("a4-4.html", title="ファイルの書き込み", message="")
    
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")