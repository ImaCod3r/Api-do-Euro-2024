from flask_cors import CORS
from routes.matches import matches
from routes.home import home 
from routes.docs import docs

def routes_config(api):
    CORS(api)
    api.register_blueprint(home)
    api.register_blueprint(matches)
    api.register_blueprint(docs)
    
# By Imacod3r