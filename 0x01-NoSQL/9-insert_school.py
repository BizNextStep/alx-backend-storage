#!/usr/bin/env python3
"""
This module provides a function to insert a new document in a MongoDB collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the collection based on kwargs.
    Returns the new _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))
    
    from 8-all import list_all
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))

