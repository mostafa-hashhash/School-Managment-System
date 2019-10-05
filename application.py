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
	return redirect(url_for('login'))





@app.route("/student")
def follow():
	
	tid = var.teacher_id
	lec = lecture.query.filter_by(teacher_id = tid).all

	x = lecture.query.all()
	return render_template("follow.html",lectures=x)

@app.route("/teacher")
def teacher():
	pass


@app.route("/admin")
def admin():
	pass




@app.route("/logout")
def logout():
	key_list = list(session.keys())
	for key in key_list:
		session.pop(key)
	return redirect(url_for('login'))




@app.route("/login",methods=["GET", "POST"])
def login():

	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 

		loged = user.query.filter_by(name=user_name, password=password).first()
		if loged is not None:
			session["user_name"] = user_name
			session["password" ] = password
			session["uid"] = loged.id
			session["type"] = "s"
			return redirect(url_for('student',var=loged ) )
		
		loged = teacher.query.filter_by(name=user_name, password=password).first()
		if loged is not None:
			session["user_name"] = user_name
			session["password" ] = password
			session["uid"] = loged.id
			session["type"] = "t"
			return redirect(url_for('teacher',var=loged ) )
		
		loged = admin.query.filter_by(name=user_name, password=password).first()
		if loged is not None:
			session["user_name"] = user_name
			session["password" ] = password
			session["uid"] = loged.id
			session["type"] = "a"
			return redirect(url_for('admin',var=loged ) )
	else: ## request.method == "GET"
		if "user_name" not in session and "password" not in session :
			return render_template("login.html")
		else:
			user_name = session["user_name"]
			password = session["password"]
			if session["type"] == "s":
				login = user.query.filter_by(name=user_name, password=password).first()
				return redirect(url_for('student',var=loged ) )
			if session["type"] == "t":
				login = teacher.query.filter_by(name=user_name, password=password).first()
				return redirect(url_for('teacher',var=loged ) )
			if session["type"] == "a":
				login = admin.query.filter_by(name=user_name, password=password).first()
				return redirect(url_for('admin',var=loged ) )




@app.route("/register/<string:x>", methods=["GET", "POST"])
def register(x):
	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 
		email = request.form.get('email')
		phone = request.form.get('phone')
		age = request.form.get('age')

		if obj == "Student":
			tid = request.form.get('tid')
			add_user(user_name,password,email,age,phone,tid)
			session["user_name"] = user_name
			session["password" ] = password
		elif obj == "Teacher":
			add_teacher(user_name,password,email,age,phone)
			session["user_name"] = user_name
			session["password" ] = password
		elif obj == "Admin":
			add_admin(user_name,password,email,age,phone)
			session["user_name"] = user_name
			session["password" ] = password

		return render_template("login.html")

	else:
		return render_template("register.html", x = obj)