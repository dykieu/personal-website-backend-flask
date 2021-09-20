from typing import Collection
from pymongo import MongoClient
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