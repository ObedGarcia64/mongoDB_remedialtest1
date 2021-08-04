from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
from werkzeug.wrappers import response
import db_config as database

#resources
from res.cars import Badge

app=Flask(__name__)
api=Api(app)



all_data = database.db.Badge.find()

api. add_resource(Badge,'/new/','/<string:by>:<string:data>/')
    
if __name__ == '__main__':
    app.run(load_dotenv=True)