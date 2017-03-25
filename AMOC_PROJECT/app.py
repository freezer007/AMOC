from flask import Flask, render_template, redirect, url_for, request, session, flash
from database import Database
from user import User

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/user_register')
def reg():
	return render_template("register.html")

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/form', methods=['GET'])
def form_page():
	return render_template("form.html")

@app.route('/register', methods=['POST'])  # use post we can write ['get','post']
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template('form.html')

if __name__ == '__main__':
	app.run(debug = True)
