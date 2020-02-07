"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import requests
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
data = requests.get('https://assets.breatheco.de/apis/fake/zips.php').json()
data = create_datastructure(data)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/zipcode', methods=['POST', 'GET'])
def find_new_city(data, city_name):
    info = []
    for key in data.keys():
        if data[key] == a:
            info.append({
                'zip_code': key,
                **data[key]
            })
    return info

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    if request.method == 'POST':

        json = request.get_json()
        print(json["name"])
        print(json["age"])

        return jsonify(json["age"])
    if request.method == 'GET':
        return 'You used a GET method'

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
