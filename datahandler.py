import json

def get_data():
    with open('data.json', encoding="utf-8") as file:
        data = json.load(file)
    
    matches = data.get("matches")
    return matches

# By Imacod3r :)