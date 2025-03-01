#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:28:31 2025

@author: zachariahgarr_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        """ initialize MongoDB connection"""
        USER = 'aacuser'
        PASS = 'CS340PASS'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31990
        DB = 'aac'
        COL = 'animals'
        
        """Start Connection"""
        try:
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print ("Connection Successful")
        except Exception as e:
                print(f"Failed to connect to database: {e}")
        
        
    def create(self, data):
        """Insert Document"""
        try:
            if data:
                result = self.database.animals.insert_one(data)
                return result
            else:
                raise ValueError("Data cannont be empty or None")
        except Exception as e:
                print(f"Error Creating Document: {e}")
                return None
            
    def read(self, query={}):
        """ Read documents matching query """
        try:
            result = list(self.database.animals.find(query))  # Convert cursor to list
            return result
        except Exception as e:
            print(f"Error reading documents: {e}")
            return []
            
    def update(self, query, new_values):
        """Update documents"""
        try:
            if query and new_values:
                result = self.database.animals.update_many(query, {"$set": new_values})
                return result.modified_count
            else:
                raise ValueError("Query and update values cannot be empty")
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0
            
    def delete(self, query):
        """Delete documents"""
        try:
            if query:
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            else:
                raise ValueError("Query cannot be empty")
        except Exception as e:
            print(f"Error deleting document: {e}")
            return 0
            
 # New methods for filter queries
    def get_water_rescue_dogs(self):
        return self.read({
            'breed': {'$in': ['Labrador Retriever Mix', 'Chesapeake Bay Retriever', 'Newfoundland']},
            'sex_upon_outcome': 'Intact Female',
            'age_upon_outcome_in_weeks': {'$gte': 26, '$lte': 156}
        })

    def get_mountain_rescue_dogs(self):
        return self.read({
            'breed': {'$in': ['German Shepherd', 'Alaskan Malamute', 'Old English Sheepdog', 'Siberian Husky', 'Rottweiler']},
            'sex_upon_outcome': 'Intact Male',
            'age_upon_outcome_in_weeks': {'$gte': 26, '$lte': 156}
        })

    def get_disaster_rescue_dogs(self):
        return self.read({
            'breed': {'$in': ['Doberman Pinscher', 'German Shepherd', 'Golden Retriever', 'Bloodhound', 'Rottweiler']},
            'sex_upon_outcome': 'Intact Male',
            'age_upon_outcome_in_weeks': {'$gte': 20, '$lte': 300}
        })

    def get_all_dogs(self):  # For RESET
        return self.read({})