from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/api/comments/', methods=['GET', 'POST'])
def index():
    return "It's Comments"


@app.route('/api/general/', methods=['GET', 'POST'])
def hello():
    return "It's general"


if __name__ == '__main__':
    app.run(debug=True)
