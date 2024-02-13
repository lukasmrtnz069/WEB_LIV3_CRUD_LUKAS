from flask import Flask
from TurnFight.auth import bp as auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
