import os
from flask import Flask, render_template, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/yelp')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/home')
def base():
    return render_template('base.html')

@app.route('/home/<username>')
def about(username):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    if username == "PaulinAlcoser":
        json_url = os.path.join(SITE_ROOT, "static/data", "Paulin.json")
        data = json.load(open(json_url))
        return render_template('about.html', data=data)
    elif username == "AlexisGray":
        json_url = os.path.join(SITE_ROOT, "static/data", "alexis.json")
        data = json.load(open(json_url))
        return render_template('about.html', data=data)
    else: 
        return "<h1>Username did not match</h1>"
