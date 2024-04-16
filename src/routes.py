#Purpose: Use models in my python application.
from flask import render_template, request, jsonify, Response

from models import Person
import json


def register_routes(app, db):

    @app.route('/person', methods = ['POST'])
    def createPerson():
        print("API to create a person!")

        payload = request.json
        status_code, message = 200, {}

        person = Person.query.filter(Person.email == payload["email"])

        if person.count() > 0:
            message = {"message": "Existing user!"}
            status_code = 400
        else:
            person = Person(payload["name"], payload["email"], payload["age"])
            db.session.add(person)
            db.session.commit()
            message = payload
            message["message"] = "Person is created!"
            status_code = 201

        response = app.response_class(response=json.dumps(message),
                                  status=status_code,
                                  mimetype='application/json')
   
        return response
    

    
    @app.route('/person', methods = ['PUT'])
    def updatePerson():
        print("API to update person!")

        payload = request.json
        status_code, message = 200, {}

        person = Person.query.filter(Person.email == payload["email"])

        if person.count() == 0:
            message = {"message": "Person is not found!"}
            status_code = 400
        else:
            person = person[0]
            person.name = payload["name"]
            person.age = payload["age"]
            db.session.commit()
            message = payload
            message["message"] = "Person details are updated!"

        response = app.response_class(response=json.dumps(message),
                                  status=status_code,
                                  mimetype='application/json')
   
        return response
    
    @app.route('/person/<email>', methods = ['GET'])
    def getPerson(email):
        print("API to add person!", email)

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
