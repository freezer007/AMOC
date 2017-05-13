from flask import Flask, render_template, redirect, url_for, request, session, flash
from database import Database
from user import User

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/google_login')
def google_login():
    gmail = request.form['email']
    uname = request.form['uname']
    page_photo = request.form['photolink']
    person = Database.find_one("users", {"email": gmail})
    if person is not None:  # check weather user exists or not
        return render_template("form.html", email=gmail, uname=uname, photolink=page_photo)
    else:
        return render_template("profile(updated).html")


@app.route('/facebook_login')
def google_login():
    email = request.form['email']
    uname = request.form['uname']
    page_photo = request.form['photolink']
    person = Database.find_one("users", {"email": email})
    if person is not None:  # check weather user exists or not
        return render_template("form.html", email=email, uname=uname, photolink=page_photo)
    else:
        return render_template("profile(updated).html")


if __name__ == '__main__':
    app.run(debug=True)
