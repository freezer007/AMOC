from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/form/uname', methods=['GET'])
def form_page():
	return render_template("form.html")

if __name__ == '__main__':
	app.run(debug = True)
