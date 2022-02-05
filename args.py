from flask_restful import reqparse

post_args = reqparse.RequestParser()
post_args.add_argument('_id', type=int, help='need an id', required=True)
post_args.add_argument('firstName', type=str, help='need a firstName', required=True)
post_args.add_argument('lastName', type=str, help='need a lastName', required=True)
post_args.add_argument('email', type=str, help='need an email', required=True)
post_args.add_argument('phoneNumber', type=str, help='need an phoneNumber', required=True)
post_args.add_argument('relatedTopics', type=str, help='need an relatedTopics', required=True)

put_args = reqparse.RequestParser()
put_args.add_argument('_id', type=int, help='need an id', required=True)
put_args.add_argument('firstName', type=str, help='need a firstName', required=False)
put_args.add_argument('lastName', type=str, help='need a lastName', required=False)
put_args.add_argument('email', type=str, help='need an email', required=False)
put_args.add_argument('phoneNumber', type=str, help='need an phoneNumber', required=False)
put_args.add_argument('relatedTopics', type=str, help='need an relatedTopics', required=False)


