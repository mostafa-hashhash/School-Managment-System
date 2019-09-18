from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	age =db.Column(db.Integer)
	phone =db.Column(db.Integer)
	email = db.Column(db.String(50))
	password = db.Column(db.String(50))
	status = db.Column(db.String(10))

	def __init__ (self,name,password,email,phone, age):
		user.password =  password
		user.phone = phone
		user.age = age
		user.name = name
		user.email = email
	
	def add_user(name,password,email,age,phone):
		u = User(name=name,age=age,email=email,phone=phone,password=password)
		db.session.add(u)
		db.session.commit()


class Session(db.Model):
	__tablename__ = "session"
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(40))
	content = db.Column(db.String(100))
	date = db.Column(db.Time(40))

	def __init__ (self,title,content,date):
		session.title =  title
		session.content = content
		session.date = date
	
	def add_session(title,content,date):
		u = Session(title=title,content=content,date=date)
		db.session.add(u)
		db.session.commit()


class Teacher(db.Model):
	__tablename__ = "teacher"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	age =db.Column(db.Integer)
	phone =db.Column(db.Integer)
	email = db.Column(db.String(50))
	password = db.Column(db.String(50))

	def __init__ (self,name,password,email,phone, age):
		teacher.password =  password
		teacher.phone = phone
		teacher.age = age
		teacher.name = name
		teacher.email = email
	
	def add_teacher(name,password,email,age,phone):
		u = Teacher(name=name,age=age,email=email,phone=phone,password=password)
		db.session.add(u)
		db.session.commit()

class Admin(db.Model):
	__tablename__ = "admin"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	password = db.Column(db.String(50))
