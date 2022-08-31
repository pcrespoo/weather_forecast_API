import json
from flask import Flask, request, jsonify, abort
from flask_pymongo import PyMongo
from credentials import *
from bson import json_util

app = Flask(__name__)

database_name = 'raizenAPI'
password = mongo_database_password
DB_URI = 'mongodb+srv://{}:{}@pcrespoo.ehg5dlx.mongodb.net/{}?retryWrites=true&w=majority'.format(database_user,password, database_name)

app.config['MONGO_DBNAME'] = database_name
app.config['MONGO_URI'] = DB_URI

mongo = PyMongo(app)

@app.route('/forecasts',methods=['GET'])
def get_all_forecasts():
    weather = mongo.db.weather

    output = []
    for q in weather.find():
        output.append(json.loads(json_util.dumps(q)))

    return jsonify({'results': output})

@app.route('/forecasts/<int:id>',methods=['GET'])
def get_city_forecast(id):
    weather = mongo.db.weather

    output = []
    q = weather.find({'city.id': id})
    if q:
        for item in q:
            output.append(json.loads(json_util.dumps(item)))
    
    if len(output) == 0:
        output.append('ID nao encontrado')

    return jsonify({'results': output})


if __name__ == '__main__':
    app.run(debug=True)
