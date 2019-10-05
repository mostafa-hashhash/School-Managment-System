from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class user(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable = False)
	age =db.Column(db.Integer,nullable = False)
	phone =db.Column(db.Integer,nullable = False)
	email = db.Column(db.String(50),nullable = False)
	password = db.Column(db.String(50),nullable = False)
	status = db.Column(db.String(10),nullable = False)
	teacher_id = db.Column(db.Integer, nullable = False)

	def __init__ (self,name,password,email,phone,age,status,tid):
		user.password =  password
		user.phone = phone
		user.age = age
		user.name = name
		user.email = email
		user.status = status
		user.teacher_id = tid

	def add_user(name,password,email,age,phone,tid,status):
		u = user(name=name,age=age,email=email,phone=phone,password=password,status=status,tid=tid)
		db.session.add(u)
		db.session.commit()



class lecture(db.Model):
	__tablename__ = "lecture"
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(40), nullable = False)
	content = db.Column(db.String(200),nullable = False)
	date = db.Column(db.Time(60),nullable = False)
	hw = db.Column(db.String(500),nullable = False)
	teacher_id = db.Column(db.Integer, nullable = False)

	def __init__ (self,title,content,date,tid,hw):
		lecture.title =  title
		lecture.content = content
		lecture.date = date
		lecture.teacher_id = tid
		lecture.hw = hw
	
	def add_lecture(title,content,date,tid,hw):
		u = lecture(title=title,content=content,date=date,tid=tid,hw=hw)
		db.lecture.add(u)
		db.lecture.commit()



class teacher(db.Model):
	__tablename__ = "teacher"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable = False)
	age = db.Column(db.Integer, nullable = False)
	phone = db.Column(db.Integer, nullable = False)
	email = db.Column(db.String(50), nullable = False)
	password = db.Column(db.String(50), nullable = False)

	def __init__ (self,name,password,email,phone, age):
		teacher.password =  password
		teacher.phone = phone
		teacher.age = age
		teacher.name = name
		teacher.email = email
		
	def add_teacher(name,password,email,age,phone):
		u = teacher(name=name,age=age,email=email,phone=phone,password=password)
		db.session.add(u)
		db.session.commit()



class admin(db.Model):
	__tablename__ = "admin"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable = False)
	password = db.Column(db.String(50),nullable = False)
	age = db.Column(db.Integer, nullable = False)
	phone = db.Column(db.Integer, nullable = False)
	email = db.Column(db.String(50), nullable = False)
	
	def __init__ (self,name,password,email,age,phone):
		admin.name =  name
		admin.password = password
		admin.email = email
		admin.phone = phone
		admin.age = age
		
	def add_admin(name,password,email,age,phone):
		u = admin(name=name,password=password,email=email,age=age,phone=phone)
		db.session.add(u)
		db.session.commit()
