from flask import Blueprint, jsonify

home = Blueprint("home", __name__)

@home.route("/", methods = ["GET"])
def main():
    info = {
        "made by": "Imacod3r",
        "version": "1.01"
    }
    
    return jsonify(info)

# By Imacod3r