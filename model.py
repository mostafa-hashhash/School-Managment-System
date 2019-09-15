class user(db.Model):
	Id = db.Column(db.Integer, primary_key=True)
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

class session(db.Model):
	Id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(40))
	content = db.Column(db.String(100))
	date = db.Column(db.Time(40))

	def __init__ (self,title,content,date,phone, age):
		session.title =  title
		session.content = content
		session.age = age
		session.date = date


class teacher(db.Model):
	Id = db.Column(db.Integer, primary_key=True)
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

class admin(db.Model):
	name = db.Column(db.String(50))
	password = db.Column(db.String(50))

