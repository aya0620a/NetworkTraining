import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template():
    dt = datetime.datetime.now()
    if(dt.second % 2 == 0):
        color = "blue"
    if(dt.second % 2 == 1):
        color = "red"
        
    message = "現在時刻は{a}時{b}分{c}秒です．".format(a=dt.hour, b=dt.minute, c=dt.second)
    
    return render_template("a2_2.html", title="現在時刻", message=message, color=color)
    # sample2-2.htmlの{{title}}と{{message}}の部分をそれぞれ置換する．


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")