from flask import Flask
from settings import *
import os

app = Flask(__name__)

routes_config(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)