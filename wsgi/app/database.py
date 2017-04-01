from app import app
from flask_pymongo import PyMongo
from flask import jsonify
import os

#app.config['MONGO_DBNAME'] = os.environ['pe301apitest1']

app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + os.environ['OPENSHIFT_APP_NAME']

mongo = PyMongo(app)

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
	#return "hello"
	return jsonify({'result' : mongo.db.collection_names()})
