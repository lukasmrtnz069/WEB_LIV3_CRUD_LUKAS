from flask import Flask, redirect, url_for

from TurnFight.auth import bp as auth_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)


@app.route('/')
def main_page():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run()
