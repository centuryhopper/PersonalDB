import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource, abort, marshal_with
from RestfulResources import *
from args import *

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL").replace(
    "postgres://", "postgresql://", 1
)
api = Api(app)

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)


class ContactModel(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phoneNumber = db.Column(db.String, nullable=False)
    relatedTopics = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Contact(_id = {self._id}, firstName = {self.firstName}, lastName = {self.lastName}, email = {self.email}, phoneNumber = {self.phoneNumber}, relatedTopics = {self.relatedTopics})"


class Contact(Resource):
    @marshal_with(contact_resource_fields)
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
        return "<h1>Added a User!</h1>"

    @marshal_with(contact_resource_fields)
    def get(self, contact_id):
        result = ContactModel.query.filter_by(_id=contact_id).first()
        if not result:
            abort(404, message="Could not find contact with that id")
        return result

    @marshal_with(contact_resource_fields)
    def put(self, contact_id):
        args = put_args.parse_args()
        result = ContactModel.query.filter_by(_id=contact_id).first()
        if not result:
            abort(404, message="Contact doesn't exist, cannot update")
        if args["firstName"]:
            result.firstName = args["firstName"]
        if args["lastName"]:
            result.lastName = args["lastName"]
        if args["email"]:
            result.email = args["email"]
        if args["phoneNumber"]:
            result.phoneNumber = args["phoneNumber"]
        if args["relatedTopics"]:
            result.relatedTopics = args["relatedTopics"]
        db.session.commit()
        return result

    def delete(self, contact_id):
        result = ContactModel.query.filter_by(_id=contact_id).first()
        if not result:
            abort(404, message="Contact doesn't exist, cannot delete")
        db.session.delete(result)
        db.session.commit()
        return "contact deleted", 204


class ContactList(Resource):
    @marshal_with(contact_resource_fields)
    def get(self):
        return ContactModel.query.all()


@app.route("/test", methods=["GET", "POST", "PUT", "DELETE"])
def index():
    return "<h1>If you see this, then this api has been properly deployed</h1>"


@app.route("/api/v1/count", methods=["GET", "POST", "PUT", "DELETE"])
def count():
    return str(len(ContactModel.query.all()))


api.add_resource(Contact, "/api/v1/<int:contact_id>")
api.add_resource(ContactList, "/api/v1/all")


if __name__ == "__main__":
    app.run()
