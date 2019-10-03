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
	course_id = db.Column(db.Integer, nullable = False)

	def __init__ (self,name,password,email,phone,age,status,cid):
		user.password =  password
		user.phone = phone
		user.age = age
		user.name = name
		user.email = email
		user.status = status
		user.course_id = cid

	def add_user(name,password,email,age,phone):
		u = user(name=name,age=age,email=email,phone=phone,password=password,status=status,cid=cid)
		db.session.add(u)
		db.session.commit()





class lecture(db.Model):
	__tablename__ = "lecture"
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(40), nullable = False)
	content = db.Column(db.String(100),nullable = False)
	date = db.Column(db.Time(40),nullable = False)
	course_id = db.Column(db.Integer, nullable = False)

	def __init__ (self,title,content,date,cid):
		lecture.title =  title
		lecture.content = content
		lecture.date = date
		lecture.course_id = cid
	
	def add_lecture(title,content,date):
		u = lecture(title=title,content=content,date=date,cid=cid)
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
	course_id = db.Column(db.Integer, nullable = False)
	def __init__ (self,name,password,email,phone, age,cid):
		teacher.password =  password
		teacher.phone = phone
		teacher.age = age
		teacher.name = name
		teacher.email = email
		teacher.course_id = cid
		
	def add_teacher(name,password,email,age,phone):
		u = teacher(name=name,age=age,email=email,phone=phone,password=password,cid=cid)
		db.session.add(u)
		db.session.commit()





class admin(db.Model):
	__tablename__ = "admin"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable = False)
	password = db.Column(db.String(50),nullable = False)
	teacher_id = db.Column(db.Integer, nullable=False)
	course_id = db.Column(db.Integer, nullable=False)
	
	def __init__ (self,name,password,tid,cid):
		admin.name =  name
		admin.password = password
		admin.teacher_id = tid
		admin.course_id = cid
		
	def add_admin(name,password):
		u = admin(name=name,password=password,tid=tid,cid=cid)
		db.session.add(u)
		db.session.commit()




"""
class course(db.Model):
	__tablename__ = "admin"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable = False)
	teacher_id = db.Column(db.Integer,nullable = False)
	lecture_id = db.Column(db.Integer,nullable = False)
	hw = db.Column(db.String(500),nullable = False)

	def __init__ (self,name,tid,lid,hw):
		course.name = name
		courser.teacher_id = tid
		course.lecture_id = lid
		course.hw = hw
	
	def add_course(name,tid,lid,hw):
		u = course(name=name,tid=tid,lid=lid,hw=hw)
		db.session.add(u)
		db.session.commit()
"""