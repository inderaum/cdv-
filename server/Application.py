from flask import Flask
import sqlalchemy

app = Flask(__name__)


@app.route("/")
def hello():
    return "sqlalchemy version" + sqlalchemy.__version__


if __name__ == '__main__':
    app.run(debug=True)
