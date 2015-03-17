from app import db

class Festival(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256), index=True, unique=True)
	description = db.Column(db.Text())
	starttime = db.Column(db.TIMESTAMP())
	def __repr__(self):
		return '<Festival %r>' % self.name 
	