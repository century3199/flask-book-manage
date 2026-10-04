from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# 数据库连接函数
def get_db():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="", #这里改成你自己mysql密码！
        database="book_manage",
        charset="utf8mb4"
    )
    return conn

# 首页：展示所有图书
@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, book_name, author FROM book")
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", books=books)

# 添加图书页面
@app.route('/add', methods=["GET","POST"])
def add_book():
    if request.method == "POST":
        name = request.form["book_name"]
        author = request.form["author"]
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO book(book_name, author) VALUES(%s,%s)", (name, author))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    return render_template("add.html")

# 删除图书
@app.route('/delete/<int:bid>')
def delete(bid):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=%s", bid)
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
