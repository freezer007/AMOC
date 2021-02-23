from flask import Flask
from flask import render_template
from flask import request
from flask import session

from common.database import Database
from models.user import User

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')  # FOR IMPORT USE ALT + IMPORT
def hello_world():
    return render_template('login.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/login', methods=['post'])  # use post we can write ['get','post']
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run(port=80)
