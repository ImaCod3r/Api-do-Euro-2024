from flask import Blueprint, render_template, url_for

docs = Blueprint("docs", __name__, url_prefix="/docs")

@docs.route("/", methods=["GET"])
def main():
    media = {
        "img1": url_for('static', filename = 'sample1.png'),
        "img2": url_for('static', filename = 'sample2.png')
    }
    
    return render_template('docs_page.html', media = media)