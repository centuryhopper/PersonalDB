from secrets import Secrets
from pymongo import MongoClient

'''
cluster
    - database
        - collection
            - bson data

'''

client = MongoClient(f"mongodb+srv://{Secrets.mongoUser}:{Secrets.mongopwd}@cluster0.pti3a.mongodb.net/{Secrets.dbName}?retryWrites=true&w=majority")
db = client[Secrets.dbName]
# collection = db[Secrets.collectionName]


# print(client.list_database_names())
# print(db.list_collection_names())

# should be a list of dicts
# add contacts here
# contacts = [

# ]


# collection.insert_many(contacts)

'''
>>> dir(collection)
['_BaseObject__codec_options', '_BaseObject__read_concern', '_BaseObject__read_preference', '_BaseObject__write_concern', '_Collection__create', '_Collection__create_indexes', '_Collection__database',
'_Collection__find_and_modify', '_Collection__full_name', '_Collection__name', '_Collection__write_response_codec_options', '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_aggregate', '_aggregate_one_result', '_command', '_count_cmd', '_delete', '_delete_retryable', '_insert_one', '_read_preference_for', '_socket_for_reads', '_socket_for_writes', '_update', '_update_retryable', '_write_concern_for', '_write_concern_for_cmd', 'aggregate', 'aggregate_raw_batches', 'bulk_write', 'codec_options', 'count_documents', 'create_index', 'create_indexes', 'database', 'delete_many', 'delete_one', 'distinct', 'drop', 'drop_index', 'drop_indexes', 'estimated_document_count', 'find', 'find_one', 'find_one_and_delete', 'find_one_and_replace', 'find_one_and_update', 'find_raw_batches', 'full_name', 'index_information', 'insert_many', 'insert_one', 'list_indexes', 'name', 'next', 'options', 'read_concern', 'read_preference', 'rename', 'replace_one', 'update_many', 'update_one', 'watch', 'with_options', 'write_concern']
'''




