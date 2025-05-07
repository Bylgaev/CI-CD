# app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    message = 'Добро пожаловать! Проверка окончания лабы 1'
    return render_template('index.html', message=message)
