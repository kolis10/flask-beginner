"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import requests
import json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Person, Zipcode



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/zipcode', methods=['POST', 'GET'])
def handle_zip():

    zip = request.get_json()

    with open('src/zipcodes.json','r') as f:
        zipcodes = json.load(f)

    direct = zipcodes[zip["zip"]]
    db.session.add(Zipcode(
        city = direct["city"],
        state = direct["state"],
        latitude = direct["latitude"],
        longitude = direct["longitude"],
        population = direct["population"],
        zip_code = direct["zip"]

    ))
    db.session.commit()
    print(zipcodes[zip["zip"]])    
    return 'successfully made'

@app.route('/all_zips', methods=['POST', 'GET'])
def handle_all_zips():

    with open('src/zipcodes.json','r') as f:
        zipcodes = json.load(f)

    # for key in zipcodes.keys():
    #     z = zipcodes[key]
    #     db.session.add(Zipcode(
    #         city = z["city"],
    #         state = z["state"],
    #         latitude = z["latitude"],
    #         longitude = z["longitude"],
    #         population = z["population"],
    #         zip_code = z["zip"]

    #     ))
    for v in zipcodes.values():
        db.session.add(Zipcode(
            city = v["city"],
            state = v["state"],
            latitude = v["latitude"],
            longitude = v["longitude"],
            population = v["population"],
            zip_code = v["zip"]

        ))
    
    db.session.commit()
    return 'success'

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    if request.method == 'POST':

        json = request.get_json()
        print(json["name"])
        print(json["age"])

        return jsonify(json["age"])
    if request.method == 'GET':
        return 'You used a GET method'

@app.route('/register')
def register():
    json = request.get_json()
    info = Person(
        username = json['username'],
        email = json['email']
    )
    db.session.add(info)
    db.session.commit()
    return 'user added'

@app.route('/login', methods=['POST']) 
def handle_login():

    if request.method == 'POST':

        json = request.get_json()
        if json["username"] == "Cassie_Enyella" and json["password"] == "r@j_RAG3":
            return "Correct Credentials"
        else:
            return "Incorrect Imbecile"

    if request.method == 'GET':
        return 'You used a GET method'


@app.route('/hola', methods=['POST']) #Without the GET method we will not be able to see this page on the browser
def handle_hola():

    response_body = "hola"

    return jsonify(response_body), 200

@app.route('/howdy', methods=['POST', 'GET'])
def handle_howdy():

    response_body = """
        <img src='https://media3.giphy.com/media/2UZOwpcXbwPe0/giphy.gif'/>
        <h1>Howdy Y'all!!</h1>"""


    return response_body

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
