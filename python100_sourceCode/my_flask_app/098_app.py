import sqlite3
import os
from flask import Flask, render_template 

app = Flask(__name__)

root_dir = os.path.dirname(__file__) 
db = os.path.join(root_dir, 'danawa.sqlite')

@app.route('/')
def show_whishlist():
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute('SELECT title, price, link from Product order by id desc')
        items = cur.fetchall()
        return render_template('my_app.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)