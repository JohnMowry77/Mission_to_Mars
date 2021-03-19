from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app=Flask(__name__)

# Use flast_pymongo to set up mongo connection
app.config["MONGO_URI"] ="mongodb://localhost:27017/mars_db_one"
mongo=PyMongo(app)

@app.route('/')
def index():
	mongo_data=mongo.db.mars_info.find_one()
	#print(list(data_from_mongo))	
	if mongo_data:
		return render_template('index.html', mars_info=mongo_data)
	else:
		return 'Error Try Again'
	#return render_template('index.html', dict=data_from_mongo)

#create a new route:
@app.route('/scrape')
def scrape():
	mars = mongo.db.mars_info
	mars_data= scrape_mars.scrape()
	#print(mars_data)
	mars.update({}, mars_data, upsert=True)
	

# 	print ('clicked button') #it needs to call the scrape_mars.py. 

# 	what is important is that it will return a dict of results
# 	# store the dict of results to mongo using client.mars_db_one.mars_info.insert(, upsert=True)
#	mars_info=

# 	data_from_mongo=client.mars_db_one.find_one()

# 	return render_template('index.html', data_from_flask=data_from)
# 	call the scrape_mars.py, which will retrun a dict of ....

# 	store the dict of results to mongodb 

	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)