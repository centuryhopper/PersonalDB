from flask import Blueprint
from flask_restful import reqparse
from .extensions import mongo


main = Blueprint('main', __name__)

post_args= reqparse.RequestParser()
post_args.add_argument('id', type=int, help='need an id', required=True)
post_args.add_argument('firstName', type=str, help='need a firstName', required=True)
post_args.add_argument('lastName', type=str, help='need a lastName', required=True)
post_args.add_argument('email', type=str, help='need an email', required=True)



@main.route('/')
def index():
    return '<h1>Welcome to the main page!</h1>'

@main.route('/get/id/<int:val>', methods=['GET'])
def get(val):
    user_collection = mongo.db.Contacts
    query = user_collection.find_one({'id' : val})
    return query

# http://127.0.0.1:5000/post?id=0&firstName=Molt&lastName=Klaus&email=molt_klaus_email.com
@main.route('/post', methods=['POST'])
def post():
    user_collection = mongo.db.Contacts
    args = post_args.parse_args()
    user_collection.insert_one({'id': args['id'], 'firstName' : args['firstName'], 'lastName' : args['lastName'], 'email' : args['email']})
    return '<h1>Added a User!</h1>'

# @main.route('/put/firstName/<fs>/<newFs>')
# def put(val, newVal):
#     user_collection = mongo.db.Contacts
#     user_collection.update_one({'firstName' : val})
#     return '<h1>Added a User!</h1>'

@main.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    user_collection = mongo.db.Contacts
    query = user_collection.find_one({'id' : id})
    if not query:
        return '<h1>This user does not exist</h1>'
    user_collection.delete_one({'id' : id})
    return '<h1>Deleted a User!</h1>'



