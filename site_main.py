from flask import *
import random
from flask_pymongo import PyMongo

t = random.randint(1,7) 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "quotes"
app.config["MONGO_URI"] = "mongodb://localhost:27017/quotes" 

mongo = PyMongo(app)

@app.route('/home')
def home():
	t = random.randint(1,7)
	user = mongo.db.quotes
	data = user.find_one({"ID": t})
	a = data['Quote']
	b = data['Author']
	return render_template('home.html', name = b, quote = a)

@app.route('/skill')
def skill():
	t = random.randint(1,7)
	user = mongo.db.quotes
	data = user.find_one({"ID": t})
	a = data['Quote']
	b = data['Author']
	return render_template('skill.html', name = b, quote = a)

@app.route('/education')
def education():
	t = random.randint(1,7)
	user = mongo.db.quotes
	data = user.find_one({"ID": t})
	a = data['Quote']
	b = data['Author']
	return render_template('education.html', name = b, quote = a)

@app.route('/projects')
def projects():
	t = random.randint(1,7)
	user = mongo.db.quotes
	data = user.find_one({"ID": t})
	a = data['Quote']
	b = data['Author']
	return render_template('projects.html', name = b, quote = a)

if __name__ == '__main__':
   app.run(debug = True)