#!/usr/bin/env python3
"""
This module provides a function to update topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    from 8-all import list_all
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

