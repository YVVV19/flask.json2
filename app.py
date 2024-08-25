from flask import Flask, render_template
from flask_http_middleware import MiddlewareManager

from db import migrate
from main2 import init_data


app = Flask(__name__)

migrate()


@app.get("/")
def index():
    dict = init_data()
    return render_template("index.html", dict_weather=dict)


if __name__ == "__main__":
    app.run(
        host="0.0.0.1",
        port=8080,
        debug=True,
    )