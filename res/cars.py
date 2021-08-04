from flask import json, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Badge(Resource):

    def get(self,by,data):
        response = self.abort_if_not_exist(by, data)
        response ['_id'] = str (response['_id'])
        return jsonify(response)
    
    def post(self):

        _id = str(database.db.Badge.insert_one({
        'serial_number':request.json['serial_number'],
        'model':request.json['model'],
        'brand':request.json['brand'],
        'year':request.json['year'],
        }).inserted_id)
        return jsonify({"_id":_id})

    def delete(self, by, data):
        response = self.abort_if_not_exist(by, data)
        database.db.Badge.delete_one({'_id':response['_id']})
        response['_id'] = str(response['_id'])
        return jsonify({"deleted":response})
    
    def put(self, by, data):

        response = self.abort_if_not_exist(by, data)

        for key, value in request.json.items():
            response[key] = value

        database.db.Badge.update_one({'_id':ObjectId(response['_id'])},
        {'$set':{
        'serial_number':request.json['serial_number'],
        'model':request.json['model'],
        'brand':request.json['brand'],
        'year':request.json['year'],


        }})
        response ['_id'] = str (response['_id'])
        return jsonify(response)

    def abort_if_not_exist(self,by,data):
        if by == "_id":
            response = database.db.Badge.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.Badge.find_one({f"{by}": data})
        if response:
            return response
        else:
            abort(jsonify({"Status":404, f"{by}":f"{data} not found"}))