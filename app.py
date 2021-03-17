from flask import Flask, render_templates
import pymongo

app=Flask(__name__)

mongo_conn='mongodb://localhost:27017'
client=pymongo.MongoClient(mongo_conn)

