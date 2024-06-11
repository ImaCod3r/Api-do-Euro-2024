from flask import Blueprint, jsonify
from datahandler import get_data

matches = Blueprint('matches',__name__, url_prefix='/matches')

data = get_data()

@matches.route("/", methods=["GET"])
def list_all():
    return data

@matches.route("/match/<int:id>", methods=["GET"])
def get_match(id):
    for match in data:
        if match["id"] == id:
            return jsonify(match)
    
    return jsonify({
        "message": "Not found"
    })
    
# By Imacod3r