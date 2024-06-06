import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("a5-1.db")
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route('/', methods=["GEt"])
def show_events():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM events")
    events = c.fetchall()
    return render_template('a5-1.html', events=events)

# @app.route('/search/<string:event_name>')
# def search_event(event_name):
#     db = get_db()
#     c = db.cursor()
#     c.execute("SELECT * FROM events WHERE event_name LIKE ?", ('%' + event_name + '%',))
#     events = c.fetchall()
#     return render_template('a5-1.html', events=events)



if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")