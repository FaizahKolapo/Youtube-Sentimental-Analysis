from flask import Flask
from app_blueprint import app_blueprint

app = Flask(__name__, static_url_path='', static_folder='static')
app.register_blueprint(app_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
