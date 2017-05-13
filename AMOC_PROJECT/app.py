import subprocess

from flask import Flask, render_template, redirect, url_for, request, session, flash
from database import Database
from user import User
from guide import Guide
import ast, json
from subprocess import call

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/user_register')
def reg():
    return render_template("form.html")


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/<username>/form', methods=['POST'])
def form_page(username):
    pages = Database.find_one("users", {"username": username})
    for page in pages:
        page_user = [page['username']]
        page_photo = [page['photolink']]
    return render_template("form.html", username=page_user, photolink=page_photo)


@app.route('/logged_out')
def logout():
    session['email'] = None
    return render_template('index.html')


@app.route('/mylogin', methods=['POST'])
def mylogin():
    email = request.form['hid3']
    name = request.form['hid2']
    photolink = request.form['hid1']
    data = Database.find_one("users", {"email": email})
    if data is None:
        return render_template('form.html', email=email, name=name, photolink=photolink)
    page = ast.literal_eval(json.dumps(data))
    User.login(page['email'])
    return render_template('user_first_page.html', name=name)


@app.route('/logged_in', methods=['POST'])
def login_page():
    username = request.form['name']
    email = request.form['email_id']
    cid = request.form['college_id']
    mob = request.form['mobile_no']
    hname = request.form['hostel_name']
    photolink = request.form['photo']
    User.register(username, email, cid, mob, hname, photolink)
    pages = Database.find_one("users", {"username": username})
    page = ast.literal_eval(json.dumps(pages))
    User.login(page['email'])
    return render_template('user_first_page.html', name=page['username'])


@app.route('/register', methods=['post'])  # use post we can write ['get','post']
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email, password)
    return render_template('form.html')


@app.route('/mentors/<string:subject>')
def mentor_page(subject):
    subject = subject.replace(' ', '')
    docs = list(Database.find("guide", {"subject": subject}))
    print docs
    posts = []
    pages = []
    for doc in docs:
        posts.append(ast.literal_eval(json.dumps(doc)))
    for post in posts:
        p = Database.find_one("users", {"username": post['uname']})
        pages.append(ast.literal_eval(json.dumps(p)))
    return render_template('mentors(updated).html', pages=pages)


@app.route('/first')
def first():
    if session['email'] is not None:
        pages = Database.find_one("users", {"email": session['email']})
        page = ast.literal_eval(json.dumps(pages))
        return render_template('user_first_page.html', name=page['username'])
    return render_template('index.html')


@app.route('/interestingsubjects')
def interestingsub():
    if session['email'] is not None:
        pages = Database.find_one("users", {"email": session['email']})
        page = ast.literal_eval(json.dumps(pages))
        return render_template('user_first_page.html', name=page['username'])
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/php')
def php():
    return reurllib2.urlopen("http://www.someURL.com/pageTracker.html").read();


@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/profile_updated', methods=['POST'])
def profile_updated():
    pages = Database.find_one("users", {"email": session['email']})
    page = ast.literal_eval(json.dumps(pages))
    subject = request.form['mentor_subject']
    subject = subject.replace(' ', '')
    subject = subject.lower()
    Guide.register(page['username'], subject)
    docs = Database.find_one("users", {"email": session['email']})
    doc = ast.literal_eval(json.dumps(docs))
    return render_template('profile.html', post=doc)


@app.route('/profile')
def profile():
    if session['email'] is not None:
        pages = Database.find_one("users", {"email": session['email']})
        print 'hello'
        print session
        page = ast.literal_eval(json.dumps(pages))
        return render_template('profile.html', post=page)
    return render_template('index.html')


@app.route('/<email>/<field>/mentor')
def guide(email, field):
    Guide.register(email, field)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
