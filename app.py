# app.py

from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index_page():

    # message = 'Добро пожаловать! Проверка окончания лабы 1'
    return "Hello from Flask CD!" # <-- Новая строка: возвращаем простой текст

    # return render_template('index.html', message=message)

