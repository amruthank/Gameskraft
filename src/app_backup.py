from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{master username}:{db password}@{endpoint}/{db instance name}'

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:admin123@database-2.c9mkqis8ciad.ap-south-1.rds.amazonaws.com:3306/flask?charset=utf8mb4"
# 
# db = SQLAlchemy(app)

# db.init_app(app)

# with app.app_context():
#     db.create_all()



conf ={
    'host':"database-2.c9mkqis8ciad.ap-south-1.rds.amazonaws.com",
    'port':'3306',
    'database':"flask",
    'user':"admin",
    'password':"admin123"
}
app.config['SQLALCHEMY_DATABASE_URI']  = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**conf)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_POOL_RECYCLE"] = {'pool_recycle' : 280}

# from sqlalchemy import create_engine
# engine = create_engine(app)
db = SQLAlchemy(app)

# db.init_app(app)
# with app.app_context():
#     db.create_all()




@app.route('/hello')
def hello_world():
    return 'Hello World'

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
    


from flask import render_template, request, jsonify, Response

# from models import Person
import json


@app.route('/person/<email>', methods = ['GET'])
def getPerson(email):
    print("API to get person details!", email)

    status_code, message = 200, {}
    person = Person.query.filter_by(email=email).first()
    if not person:
        message["message"] = "Person detail is not found!"
    else:
        message["name"] = person.name
        message["email"] = person.email
        message["age"] = person.age

    response = app.response_class(response=json.dumps(message),
                                status=status_code,
                                mimetype='application/json')

    return response


# if __name__ == '__main__':
#     app.run()