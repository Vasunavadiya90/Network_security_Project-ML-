import os
import sys
import json
from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

import certifi
ca  = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e,sys)

    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace = True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_records_mongodb(self,records,database,collection):
        try:
            
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection  =self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))

        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=='__main__':
     FILE_PATH = 'Network_data\phisingData.csv'
     DATABASE = 'VasuAi'
     collection = 'NetworkData'
     networkobj = NetworkDataExtract()
     records  = networkobj.csv_to_json_converter(FILE_PATH)
     print(records)
     length =  networkobj.insert_records_mongodb(records=records,database=DATABASE,collection=collection)
     print(f'length of the records is {length}')







