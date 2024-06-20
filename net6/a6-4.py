import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def input():
    return render_template("a6-4.html", title="フォームの利用")


@app.route("/", methods=["POST"])
def output():
    dt = datetime.datetime.now()
    name = request.form["name"]
    try:
        birth_year = dt.year - int(request.form["age"])
        message = "{}さんが生まれたのは{}年かその前の年．".format(name, birth_year)
    except Exception:
        message = "年齢が正しくありません．"
    return render_template("a6-4.html", title="フォームの利用", name=name, message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")