from flask import Blueprint
from flask_restful import reqparse
from .extensions import mongo


main = Blueprint('main', __name__)

post_args = reqparse.RequestParser()
post_args.add_argument('id', type=int, help='need an id', required=True)
post_args.add_argument('firstName', type=str, help='need a firstName', required=True)
post_args.add_argument('lastName', type=str, help='need a lastName', required=True)
post_args.add_argument('email', type=str, help='need an email', required=True)
post_args.add_argument('phoneNumber', type=str, help='need an phoneNumber', required=True)
post_args.add_argument('relatedTopics', type=str, help='need an relatedTopics', required=True)

put_args = reqparse.RequestParser()
put_args.add_argument('id', type=int, help='need an id', required=True)
put_args.add_argument('firstName', type=str, help='need a firstName', required=False)
put_args.add_argument('lastName', type=str, help='need a lastName', required=False)
put_args.add_argument('email', type=str, help='need an email', required=False)
put_args.add_argument('phoneNumber', type=str, help='need an phoneNumber', required=False)
put_args.add_argument('relatedTopics', type=str, help='need an relatedTopics', required=False)




@main.route('/')
def index():
    return '<h1>Welcome to the main page!</h1>'

@main.route('/get/id=<int:val>', methods=['GET'])
def get(val):
    user_collection = mongo.db.Contacts
    query = user_collection.find_one({'_id' : val})
    return query


@main.route('/post', methods=['POST'])
def post():
    user_collection = mongo.db.Contacts
    args = post_args.parse_args()
    user_collection.insert_one({'_id': args['id'], 'firstName' : args['firstName'], 'lastName' : args['lastName'], 'email' : args['email'], 'phoneNumber': args['phoneNumber'], 'relatedTopics': args['relatedTopics']})
    return '<h1>Added a User!</h1>'

@main.route('/put', methods=['PUT'])
def put():
    user_collection = mongo.db.Contacts
    args = put_args.parse_args()
    if args['firstName']:
        user_collection.update_one({'_id' : args['id']}, {'$set': {'firstName' : args['firstName']} })
    if args['lastName']:
        user_collection.update_one({'_id' : args['id']}, {'$set': {'lastName' : args['lastName']} })
    if args['email']:
        user_collection.update_one({'_id' : args['id']}, {'$set': {'email' : args['email']} })
    if args['phoneNumber']:
        user_collection.update_one({'_id' : args['id']}, {'$set': {'phoneNumber' : args['phoneNumber']} })
    if args['relatedTopics']:
        user_collection.update_one({'_id' : args['id']}, {'$set': {'relatedTopics' : args['relatedTopics']} })
    return '<h1>Updated a User!</h1>'

@main.route('/delete/id=<int:val>', methods=['DELETE'])
def delete(val):
    user_collection = mongo.db.Contacts
    query = user_collection.find_one({'_id' : val})
    if not query:
        return '<h1>User with this id is not found!</h1>'
    user_collection.delete_one({'_id' : val})
    return '<h1>Deleted a User!</h1>'



