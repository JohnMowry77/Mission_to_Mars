from flask import Flask, render_templates
import pymongo

app=Flask(__name__)

mongo_conn='mongodb://localhost:27017'
client=pymongo.MongoClient(mongo_conn)

@app.route('/')
def index():
	data_from_mongo=client.mars_db_one.mars_info.find_one()
	#print(list(data_from_mongo))	
	if data_from_mongo:
		return render_template('index.html', data_from_flask=data_from_mongo)
	else:
		return 'Error Try Again'
	#return render_template('index.html', dict=data_from_mongo)

create a new route:
@app.route('/scrape')
def scrape():
	mars_data= scrape_mars.scrape()
	print(mars_info)
	client.mars_db_one.mars_info.update_one({}, mars_data, upsert=True)
	

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