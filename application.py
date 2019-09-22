import os
from flask import Flask, render_template,url_for,session,request, redirect
from models import * 
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
	db.create_all()






@app.route("/")
def home():
	return render_template("login.html")
	
@app.route("/finance")
def finance():
	"""
		info about the payment status
		paid , not-yet
	"""
	return render_template("finance.html")
	
@app.route("/follow")
def follow():
	"""
		info about every lecture  
		will join the tables to get the student status at this session 
	"""
	lecture.query.filter_by(user_id = session["uid"]).all
	user.query.filter_by(id = session["uid"]).first().lecture
	db.session.query
	x = lecture.query.all()
	return render_template("follow.html",lectures=x)
	




@app.route("/delay")
def delay():
	"""
		Join The session,student Tables to get all the session for that specific user
		user data is provided in the session 
	"""
	return render_template("delay.html")





@app.route("/logout")
def logout():
	key_list = list(session.keys())
	for key in key_list:
		session.pop(key)
	return render_template("lgoin.html")






@app.route("/login",methods=["GET", "POST"])
def login():

	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 
		loged = teacher.query.filter_by(name=user_name, password=password).first()
		if loged is not None:
			session["user_name"] = user_name
			session["password" ] = password
			session["uid"] = loged.id
			return render_template('home.html',student=loged)
	else:
		if "user_name" not in session and "password" not in session :
			return render_template("login.html")
		else:
			user_name = session["user_name"]
			password = session["password"]
			login = teacher.query.filter_by(name=user_name, password=password).first()
			return render_template('home.html',student=login)







@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 
		email = request.form.get('email')
		phone = request.form.get('phone')
		age = request.form.get('age')

		x = teacher(name=user_name,age=age,email=email,phone=phone,password=password)
		db.session.add(x)
		db.session.commit()

		##teacher.add_teacher(user_name,password,email,age,phone)

		return render_template("login.html")
	return render_template("register.html")