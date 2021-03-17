from flask import Flask, render_template
import pymongo

app=Flask(__name__)

mongo_conn='mongodb://localhost:27017'
client=pymongo.MongoClient(mongo_conn)


@app.route('/')
def index():
	data_from_mongo=client.mars_db.one.find_one()
	return render_template('index.html', data_from_flask=data_from)


@app.route('/')
def index():
	data_from_mongo=client.mars_db.one.find_one()
	return render_template('index.html', data_from_flask=data_from)