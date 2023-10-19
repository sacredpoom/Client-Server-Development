# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        #Initializing the MongoClient. This helps to
        #access the MongoDB databases and collections. 
        # This is hard-wired to use the AAC database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Edit connection variables below to reflect
        # your own instance of MongoDB
        #
        # Connection Variables
        
        #USER = 'aacuser'
        #PASS = 'SNHU2024'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30207
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) #connect to Mongo
        self.database = self.client['%s' % (DB)] #connect to AAC
        self.collection = self.database['%s' % (COL)] #connect to animals collection
        print("Connection Successful") #inform user success

            
    # The C in CRUD create method
    def create(self, data):
        """ data should be dictionary key : value format, true on success """
        if isinstance(data, dict) and data: # check that input is a dict and non-empty
            self.database.animals.insert_one(data) # insert if okay and return true
            return True
        else:
            raise Exception("Invalid parameter, expected a non-empty dictionary.")
    
    # The R in CRUD read method
    def read(self, data):
        """ data should be dictionary key : value, return result on success """
        if isinstance(data, dict) and data: # check that input is dict and non-empty
            data_find = list(self.database.animals.find(data)) #data should be dict
            if data_find: #if something found
                return data_find #return
            else:
                raise Exception("No documents found for search criteria") #nothing found
        else:
            raise Exception("Invalid parameter, expected a non-empty dictionary.") #inform user of bad input
    
    # ReadAll for use with dashboard
    # return all documents
    def readAll(self):
        """ Read all documents from the 'animals' collection """
        data_find = list(self.database.animals.find({}))
        if data_find:
            return data_find
        else:
            raise Exception("No documents found.")
    
    # The U in CRUD update method
    def update(self, query, update_data):
        """ update_data is dict object, return update count """
        if query is not None and isinstance(update_data, dict): #update_data should be dict
            result = self.database.animals.update_many(query, {"$set": update_data})
            return result.modified_count
        else:
            raise Exception("Invalid input for update operation.")
            
    # The D in CRUD delete method
    def delete(self, query):
        """ deletes all matches to query """
        if query is not None and isinstance(query, dict):
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Invalid input for delete operation, expected dictionary.")