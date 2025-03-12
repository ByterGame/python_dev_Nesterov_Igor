from flask import Flask
from routes.api import api_app

app = Flask(__name__)
app.register_blueprint(api_app)

if __name__ == "__main__":
    app.run(debug=True)
