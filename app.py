from flask import Flask
from routes.api import app as api_app

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_app)
    app.run(debug=True)