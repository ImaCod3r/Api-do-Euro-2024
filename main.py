from flask import Flask
from settings import *

api = Flask(__name__)

routes_config(api)

api.run(debug=True, port=5000)