from flask import Flask, render_template

app = Flask(__name__)

event_name = ["高校卒業", "大学入学", "大学卒業"]
event_date = ["2021年3月9日", "2021年4月1日", "2026年3月31日"]
event_place = ["高校", "大学", "大学"]


@app.route("/id<num>")
# ルートがidで始まる場合に呼び出される．idより後の部分は変数numに代入される．
def page(num):
    try:
        message1 = "これは{}の詳細についてのページです．".format(event_name[int(num) - 1])
        message2 = "日程は{}で、場所は{}です".format(event_date[int(num) - 1], event_place[int(num) - 1])
    except Exception:
        # numの値が正しくない場合は例外が生じる．
        message1 = "ページは見つかりませんでした"
    return render_template("a2_3.html", title="表示テスト", message1=message1, message2=message2)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")