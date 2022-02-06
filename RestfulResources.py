
from flask_restful import fields



# how the contact model should be serialized
contact_resource_fields = {
    "_id": fields.Integer,
    "firstName": fields.String,
    "lastName": fields.String,
    "email": fields.String,
    "phoneNumber": fields.String,
    "relatedTopics": fields.String,
}











