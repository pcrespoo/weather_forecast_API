import requests
from pymongo import MongoClient
from credentials import *
import sys

database_name = 'raizenAPI'
password = mongo_database_password
DB_URI = 'mongodb+srv://{}:{}@pcrespoo.ehg5dlx.mongodb.net/{}?retryWrites=true&w=majority'.format(database_user,password, database_name)
API_KEY = api_key

myclient = MongoClient(DB_URI)
db = myclient['raizenAPI']
collection = db['weather']
city = sys.argv[1]

print('Iniciando consulta da previsão tempo para os próximos dias...')
geo_request = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}'.format(city, API_KEY))
geo_result = geo_request.json()
lat = geo_result[0]['lat']
long = geo_result[0]['lon']
weather_request = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}&units=metric'.format(lat,long, API_KEY))
weather_result = weather_request.json()
print('Consulta concluída com êxito! Salvando no DB...')
collection.insert_one(weather_result)
print('Previsões salvas com sucesso.')

