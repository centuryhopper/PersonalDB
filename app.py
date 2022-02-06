import json
import os
from flask import Blueprint, Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, abort, fields, marshal_with
from args import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
api = Api(app)

db = SQLAlchemy(app)

class ContactModel(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phoneNumber = db.Column(db.String, nullable=False)
    relatedTopics = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Contact(_id = {_id}, firstName = {firstName}, lastName = {lastName}, email = {email}, phoneNumber = {phoneNumber}, relatedTopics = {relatedTopics})"


# how the video model should be serialized
resource_fields = {
	'_id': fields.Integer,
	'firstName': fields.String,
	'lastName': fields.String,
	'email': fields.String,
	'phoneNumber': fields.String,
	'relatedTopics': fields.String,
}

class Contact(Resource):
    @marshal_with(resource_fields)
    def post(self, contact_id):
        args = post_args.parse_args()
        result = ContactModel.query.filter_by(_id=contact_id).first()
        if result:
            abort(409, message="Contact id taken...")
        user = ContactModel(
            _id=contact_id,
            firstName=args["firstName"],
            lastName=args["lastName"],
            email=args["email"],
            phoneNumber=args["phoneNumber"],
            relatedTopics=args["relatedTopics"],
        )
        db.session.add(user)
        db.session.commit()
        return '<h1>Added a User!</h1>'

    @marshal_with(resource_fields)
    def get(self, contact_id):
        result = ContactModel.query.filter_by(_id=contact_id).first()
        if not result:
            abort(404, message="Could not find contact with that id")
        return result

api.add_resource(Contact, "/contact/<int:contact_id>")

# def userExists(val:int):
#     user_collection = mongo.db.Contacts
#     query = user_collection.find_one({'_id' : val})
#     return query is not None


# @app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
# def index():
#     return "<h1>Welcome to the main page!</h1>"





# @app.route('/getAll', methods=['GET'])
# def getAll():
#     res = [doc for doc in mongo.db.Contacts.find({})]
#     # sort by _id in ascending order
#     res.sort(key=lambda doc:doc['_id'])
#     return json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '))

# @app.route('/countTotal', methods=['GET'])
# def countTotal():
#     return str(mongo.db.Contacts.count_documents({}))





# @app.route('/put', methods=['PUT'])
# def put():
#     user_collection = mongo.db.Contacts
#     args = put_args.parse_args()
#     if not userExists(args['_id']):
#         return '<h1>User with this id is not found!</h1>'
#     if args['firstName']:
#         user_collection.update_one({'_id' : args['_id']}, {'$set': {'firstName' : args['firstName']} })
#     if args['lastName']:
#         user_collection.update_one({'_id' : args['_id']}, {'$set': {'lastName' : args['lastName']} })
#     if args['email']:
#         user_collection.update_one({'_id' : args['_id']}, {'$set': {'email' : args['email']} })
#     if args['phoneNumber']:
#         user_collection.update_one({'_id' : args['_id']}, {'$set': {'phoneNumber' : args['phoneNumber']} })
#     if args['relatedTopics']:
#         user_collection.update_one({'_id' : args['_id']}, {'$set': {'relatedTopics' : args['relatedTopics']} })
#     return '<h1>Updated a User!</h1>'

# @app.route('/delete/id=<int:val>', methods=['DELETE'])
# def delete(val):
#     user_collection = mongo.db.Contacts
#     if not userExists(val):
#         return '<h1>User with this id is not found!</h1>'
#     user_collection.delete_one({'_id' : val})
#     return '<h1>Deleted a User!</h1>'


# def main():
#     app.run(debug=False, host='0.0.0.0')


# if __name__ == '__main__':
#     main()
