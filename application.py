import os
from flask import Flask, render_template,url_for,session,request
from models import * 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
	db.create_all()


@app.route("/")
def home():
	return render_template("home.html")
	
@app.route("/finance")
def finance():
	return render_template("finance.html")
	
@app.route("/follow")
def follow():
	return render_template("follow.html")
	
@app.route("/delay")
def delay():
	return render_template("delay.html")

@app.route("/logout")
def logout():
	return render_template("logout.html")


@app.route("/login",methods=["GET", "POST"])
def login():
	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 
		login = User.query.filter_by(name=user_name, password=password).first()
		if login is not None:
			return render_template('home.html',student=login)

	return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 
		email = request.form.get('email')
		phone = request.form.get('phone')
		age = request.form.get('age')
		User.add_user(user_name,password,email,age,phone)

		return render_template("login.html")
	return render_template("register.html")
