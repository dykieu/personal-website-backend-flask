from typing import Collection
from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi

class Mongo_DB:
    def __init__(self):
        self.app = None
        self.client = None
        self.db = None
        self.uri = None
    
    def init_db(self, app):
        self.app = app
        self.uri = app.config['MONGO_URI']

    def make_connection(self):
        self.client = MongoClient(self.uri, tlsCAFile=certifi.where())
        self.db = self.client['personal-website']

    def check_connection(self):
        try:
            Collection = self.db['test']
            if Collection.find_one({'test': 'ping'}):
                print(f'Mongo connection is established: {self.client}')
                return True
            else:
                raise Exception()
        except Exception as err:
            print(f'Mongo not available: {err}')
            return False

    def insert(self, collection_name, payload):
        if collection_name and payload:
            if collection_name == 'test':
                dump = {
                    'test': 'ex dump'
                }

            try:
                ins = self.db[collection_name].insert(dump)

                if ins != None:
                    print(f'Mongo Data Inserted: {ins}')
                    return ins
                else:
                    raise Exception('Unable to insert data')
            except Exception as err:
                print(f'Mongo Error: {err}')
                return None
        else:
            print('Missing collection name or payload')
            return None

    def delete(self, collection_name, payload):
        if collection_name and payload:
            try:
                find_item = self.db[collection_name].find_one({'test': payload['identifier']})
                if find_item == None:
                    raise Exception('Invalid Identifier or No entries found')
                
                deletion = self.db[collection_name].delete_one({'test': payload['identifier']})

                if deletion != None:
                    print(f'Mongo Data Deleted: {deletion}')
                    return deletion
                else:
                    raise Exception('Unable to delete data')
            except Exception as err:
                print(f'Mongo Error: {err}')
                return None
        else:
            print('Missing collection name or identifier')
            return None

    def update(self, collection_name, payload):
        if collection_name and payload:
            try:
                find_item = self.db[collection_name].find_one({'_id': ObjectId(payload['identifier'])})
                if find_item == None: raise Exception('Invalid Identified or No entries found')
                print(payload)
                print(find_item)
                updated = self.db[collection_name].update_one(
                    {'_id': ObjectId(payload['identifier'])},
                    {'$set': payload['updated_vals']})
                
                if updated != None:
                    print(f'Mongo Data updated: {updated}')
                    return None
                else: raise Exception('Unable to update data')

            except Exception as err:
                print(err)
                print('Mongo Error: {err}')
                return None
        else:
            print('Missing collection name or identified')
            return None

