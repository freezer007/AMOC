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
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()
    # email = 'first@gmail.com'
    #  password = 'first'
    # User.register(email, password)


@app.route('/reg', methods=['post'])  # use post we can write ['get','post']
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)


if __name__ == '__main__':
    app.run(port=80)
