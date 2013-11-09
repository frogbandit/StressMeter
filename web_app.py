from flask import Flask, render_template
from pymongo import MongoClient

mongo = MongoClient()
db = mongo.temp_store

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("home.html")

@app.route("/add/<name>")
def add_name(name):
   db.people.insert({
      'name': name
   })
   return "Your name is %s" % name

@app.route("/remove/<name>")
def remove_name(name):
   db.people.remove({'name': name})
   return "removed"

@app.route("/list")
def list_names():
   people = db.people.find()
   return render_template('people.html', people=people)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=5000)

