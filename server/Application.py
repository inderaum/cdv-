from flask import Flask

from db.data_source import DataSource

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
    source = DataSource()
    source.print_greeting('message')
