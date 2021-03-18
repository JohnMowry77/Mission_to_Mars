from flask import Flask, render_template, redirect
import pymongo

app=Flask(__name__)

mongo_conn='mongodb://localhost:27017'
client=pymongo.MongoClient(mongo_conn)


@app.route('/')
def index():
	data_from_mongo=client.mars_db_one.mars_info.find_one()
	#print(list(data_from_mongo))	
	return render_template('index.html', data_from_flask=data_from_mongo)
	#return render_template('index.html', dict=data_from_mongo)


# @app.route('/scrape')
# def scrape():
# 	print ('clicked button')

# 	#call the scrape_mars.py, which will return a dict of results
# 	# store the dict of results to mongo 
# 	# using client.mars_db_one.mars_info.insert(, upsert=True)
# 	data_from_mongo=client.mars_db_one.find_one()
# 	return render_template('index.html', data_from_flask=data_from)
# 	call the scrape_mars.py, which will retrun a dict of ....

# 	store the dict of results to mongodb 
# 		mars_db_one -- collection mars_info # need to add image & hemisphere images/hrefs still
	return redirect('/')

if __name__=='__main__':
	app.run(debug=True)


# @app.route('/')
# def index():
# 	data_from_mongo=client.mars_db.one.find_one()
# 	print(list(data_from_mongo))
# 	return render_template('index.html', data_from_flask=data_from_mongo)
# 	#return render_template('index.html', dict=data_from_mongo)

#Above we ar