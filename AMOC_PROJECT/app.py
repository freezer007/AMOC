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

@app.route('/<string:email>/form', methods=['GET'])
def form_page(email):
	pages = Database.find_one("users", {"email": email})
	for page in pages:
		page_user = [page['email']]
		page_photo = [page['photolink']]
	return render_template("form.html", username = page_user, photolink = page_photo)

@app.route('/register', methods=['post'])  # use post we can write ['get','post']
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email,password)
    return render_template('form.html')

@app.route('/google_login')
def google_login():
           return render_template('googlelogin.html')

if __name__ == '__main__':
	app.run(debug = True)
