
import configparser
from distutils.log import debug
import json
import os
# my-flask-app1234
from flask import Blueprint, Flask, flash, render_template, request
from flask_pymongo import PyMongo

from args import *

MONGO_URI = os.environ.get('MONGO_URI')
config = configparser.ConfigParser()
config.read('.env')
app = Flask(__name__)
app.config["MONGO_URI"] = config['MONGO_URI']['MONGO_URI']
# print(config['MONGO_URI']['MONGO_URI'])
mongo = PyMongo(app)

# type 'pipenv lock' in the terminal to create a new pipfile
# main = Blueprint('main', __name__)
# collections.find is regex friendly

def userExists(val:int):
    user_collection = mongo.db.Contacts
    query = user_collection.find_one({'_id' : val})
    return query is not None

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def index():
    return '<h1>Welcome to the main page!</h1>'

@app.route('/get/id=<int:val>', methods=['GET'])
def get(val):
    user_collection = mongo.db.Contacts
    if not userExists(val):
        return '<h1>User with this id is not found!</h1>'
    query = user_collection.find_one({'_id' : val})
    return query

@app.route('/getAll', methods=['GET'])
def getAll():
    res = [doc for doc in mongo.db.Contacts.find({})]
    # sort by _id in ascending order
    res.sort(key=lambda doc:doc['_id'])
    return json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '))

@app.route('/countTotal', methods=['GET'])
def countTotal():
    return str(mongo.db.Contacts.count_documents({}))

@app.route('/post', methods=['POST'])
def post():
    user_collection = mongo.db.Contacts
    args = post_args.parse_args()
    if userExists(args['_id']):
        return '<h1>Cannot post because a user with this id already exists!</h1>'
    user_collection.insert_one({'_id': args['_id'], 'firstName' : args['firstName'], 'lastName' : args['lastName'], 'email' : args['email'], 'phoneNumber': args['phoneNumber'], 'relatedTopics': args['relatedTopics']})
    return '<h1>Added a User!</h1>'

@app.route('/put', methods=['PUT'])
def put():
    user_collection = mongo.db.Contacts
    args = put_args.parse_args()
    if not userExists(args['_id']):
        return '<h1>User with this id is not found!</h1>'
    if args['firstName']:
        user_collection.update_one({'_id' : args['_id']}, {'$set': {'firstName' : args['firstName']} })
    if args['lastName']:
        user_collection.update_one({'_id' : args['_id']}, {'$set': {'lastName' : args['lastName']} })
    if args['email']:
        user_collection.update_one({'_id' : args['_id']}, {'$set': {'email' : args['email']} })
    if args['phoneNumber']:
        user_collection.update_one({'_id' : args['_id']}, {'$set': {'phoneNumber' : args['phoneNumber']} })
    if args['relatedTopics']:
        user_collection.update_one({'_id' : args['_id']}, {'$set': {'relatedTopics' : args['relatedTopics']} })
    return '<h1>Updated a User!</h1>'

@app.route('/delete/id=<int:val>', methods=['DELETE'])
def delete(val):
    user_collection = mongo.db.Contacts
    if not userExists(val):
        return '<h1>User with this id is not found!</h1>'
    user_collection.delete_one({'_id' : val})
    return '<h1>Deleted a User!</h1>'


def main():
    app.run(debug=False, host='0.0.0.0')


if __name__ == '__main__':
    main()


