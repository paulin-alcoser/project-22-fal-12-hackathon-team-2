import os
from flask import Flask, render_template, request
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
    if username == "PaulinAlcoser":
        return render_template('about.html')
    elif username == "AlexisGray":
        return render_template('about.html')
    else: 
        return "<h1>Username did not match</h1>"
