from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlite3 as sql
import json
#from bson.json_util import dumps

def update_task(conn, task):
    somesql = '''UPDATE products SET likes = likes + 1 WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(somesql, task)
    conn.commit()


app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userentry = request.form.get('userentry')
        conn = sql.connect("productsdb.sqlite")
        somesql1 = '''INSERT INTO totalusers (user) VALUES (?)'''
        cur = conn.cursor()
        cur.execute(somesql1, (userentry,))
        conn.commit()
        return redirect('/index')
    return render_template('login.html')

@app.route('/item/<string:id>', methods=['GET','POST']) 
def item(id):
    conn = sql.connect("productsdb.sqlite")
    conn.row_factory = sql.Row
    itemsql = '''SELECT * FROM products WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(itemsql, id)
    this_item = cur.fetchall()
    currentUser = "test1"
    if request.method == 'POST':
        try:
            with sql.connect("productsdb.sqlite") as conn:
                #Get our user
                #grabuser = '''SELECT user FROM totalusers ORDER BY id DESC LIMIT 1;'''
                #cur.execute(grabuser)
                #currentUser = cur.fetchone()
                #currentUser = currentUser['user']

                #testuser = '''SELECT * FROM actions WHERE user = ? AND id = ?'''
                #cur.execute(testuser, (currentUser, id))
                #currentUserTest = cur.fetchone()
                #cur.execute("INSERT INTO actions (id, user) VALUES (1, test)")

                #if currentUserTest==0:
                update_task(conn, (id))
                    #addlikeline = '''INSERT INTO actions (id, user) VALUES (?, ?)'''
                    #cur.execute(addlikeline, (3, "mygosh"))
                    #conn.commit()
                conn.row_factory = sql.Row
                itemsql = '''SELECT * FROM products WHERE id = ?'''
                cur = conn.cursor()
                cur.execute(itemsql, id)
                this_item = cur.fetchall()
            return render_template('/item.html', this_item = this_item, id = id)
        except:
            conn.rollback()
        finally:
            return render_template('/item.html', this_item = this_item, id = id, currentUser=currentUser)
            conn.close()
    return render_template('/item.html', this_item = this_item, id = id, currentUser=currentUser)

@app.route('/', methods=['GET'])
def index():
    conn = sql.connect("productsdb.sqlite")
    conn.row_factory = sql.Row
    cur= conn.cursor()
    cur.execute("SELECT * FROM products;")
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)