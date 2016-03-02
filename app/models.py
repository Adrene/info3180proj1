from . import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(80), unique=True)
    sex = db.Column(db.String(120), unique=True)
    image = db.Column(db.String(120), unique=True)
    
    def _init_(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def _repr_(self):
        return '<Profile %r %r>' % (self.last_name, self.first_name)