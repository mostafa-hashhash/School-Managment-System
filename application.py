from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
##from model import * 

app = Flask(__name__)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oqfjsrfqsblzha:addf88c5dcdb38f815ba5792cb835deaf4e33bfb7e4975f7ad397f002bb2bf63@ec2-54-83-9-36.compute-1.amazonaws.com:5432/d57fu9bh1mbo5f'
##app.config['SQLALCHEMY_DATABASE_URI'] = os.env.var('DB_URL')
##SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/appdb'
db = SQLAlchemy(app)

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
		user_name = request.form["name"]
		password = request.form["password"] 
		
		login = user.query.filter_by(name=user_name, password=password).first()
		if login is not None:
			return redirect(url_for("home"))

	return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		password = request.form['password']
		user_name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		age = request.form['age']

		register = user(name=user_name, email=email, password = password)
		db.session.add(register)
		db.session.commit()

		return redirect(url_for("login"))
	return render_template("register.html")


if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)