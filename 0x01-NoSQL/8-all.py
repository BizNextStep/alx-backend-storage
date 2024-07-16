#!/usr/bin/env python3
"""
This module provides a function to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in the collection.
    Returns an empty list if no document in the collection.
    """
    return list(mongo_collection.find())

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

