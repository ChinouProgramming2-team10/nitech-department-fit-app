from flask import Flask

app = Flask(__name__)


@app.route("/")
def entry():
    return "Entry Page"


if __name__ == "__main__":
    app.run(debug=True)
