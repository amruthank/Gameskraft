

from app import db, app


class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email 
        self.age = age

    def __repr__(self):
        return f'Person with {self.name} - {self.email} has age {self.age}.'
    
with app.app_context():
    db.create_all()