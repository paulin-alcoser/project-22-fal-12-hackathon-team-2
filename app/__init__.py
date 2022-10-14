import os
from flask import Flask, render_template, json
from dotenv import load_dotenv
from peewee import *
import datetime


load_dotenv()
app = Flask(__name__)


mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
        

mydb.connect()
mydb.create_tables([TimelinePost])   



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


# @app.route('/api/timeline_post', methods=['POST'])
# def post_time_line_post():
#     name = request.form['name']
#     email = request.form['email']
#     content = request.form['content']
#     timeline_post = TimelinePost.create(name=name, email=email, content=content)

#     return model_to_dict(timeline_post)

# for dirName, subdirList, fileList in os.walk(rootDir , topdown=False):
#     if dirName.endswith("1eb95ebb-d87d-4aac-XX-XX182"):
#         abs_path = os.path.join(dirName, file)
#         print('Found directory: %s' % dirName)
#         #print(fileList)
#         for file in fileList:
#             if file.endswith("activities.json"):
#                 #print('\t%s' % file)
#                 json_data = json.loads(open(abs_path).read())
#                 pprint(json_data)