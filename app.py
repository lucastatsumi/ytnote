import sqlite3
import re
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')


db_ = sqlite3.connect('database.db')
db = db_.cursor()
db.close()


@app.route("/", methods=['POST', 'GET'])
def home():
    print('OLA 1')
    if request.method == 'GET':
        print('OLA 2')
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/index", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        print('OLA 2')
        return render_template("index.html")
    elif request.method == "POST":
        nome = request.form.get("name")
        texto = request.form.get("text")
        print(nome, texto)
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/teste", methods=["GET", "POST"])
def teste():
    if request.method == "POST":
        nome = request.form.get("name")
        texto = request.form.get("text")
        url = request.form.get("url")
        if url:
            img = re.findall("([^=]*$)", url)
            print(img[0])
            print(url)
            db_ = sqlite3.connect('database.db')
            db = db_.cursor()
            db.execute(
                "INSERT INTO app (title, description, url) VALUES (?,?,?)",
                (nome, texto, img[0]))
            db_.commit()
            info = db.execute("SELECT * FROM app")
            return render_template("teste.html", teste=info)

        db_ = sqlite3.connect('database.db')
        db = db_.cursor()
        db.execute(
            "INSERT INTO app (title, description, url) VALUES (?,?,?)",
            (nome, texto, "teste"))
        db_.commit()
        info = db.execute("SELECT * FROM app")

        return render_template("teste.html", teste=info)
    else:
        return render_template("teste.html")


@app.route("/function", methods=["GET", "POST"])
def function():
    if request.method == "POST":
        value = request.form.get("botao")
        id = request.form.get("id")
        id = int(id)
        print(id)
        print(value)
        if value == "delete":
            db_ = sqlite3.connect('database.db')
            db = db_.cursor()
            info = db.execute(f"DELETE FROM app WHERE id = {id}")
            db_.commit()
            info = db.execute("SELECT * FROM app")
            return render_template("teste.html", teste=info)
        elif value == "edit":
            db_ = sqlite3.connect('database.db')
            db = db_.cursor()
            teste = db.execute(f"SELECT * FROM app WHERE id = {id}")
            for row in teste:
                info = row
            if info:
                return render_template("edit.html", teste=info)
            else:
                return render_template("edit.html")
        elif value == "mark":
            db_ = sqlite3.connect('database.db')
            db = db_.cursor()
            teste = db.execute(f"SELECT mark FROM app WHERE id = {id}")
            for row in teste:
                a = row
            if a:
                print(a)
                if a[0] == 1:
                    print("aqui")
            if a[0] == 0:
                db.execute(
                    f"UPDATE app SET mark = 1 WHERE id = {id}")
            elif a[0] == 1:
                db.execute(
                    f"UPDATE app SET mark = 0 WHERE id = {id}")
            db_.commit()
            info = db.execute("SELECT * FROM app")
            return render_template("teste.html", teste=info)

    else:
        return redirect("/")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        title = request.form.get("name")
        url = request.form.get("url")
        if url:
            img = re.findall("([^=]*$)", url)
            url = img[0]

        descripton = request.form.get("text")
        id = request.form.get("id")
        conn = sqlite3.connect('database.db')
        db = conn.cursor()
        db.execute(
            "UPDATE app SET title=?, url=?, description=? WHERE id = ?", (title, url, descripton, id))
        conn.commit()

        info = db.execute("SELECT * FROM app")
        return render_template("teste.html", teste=info)
    else:
        return render_template("edit.html")


if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=9000,
            threaded=True)
