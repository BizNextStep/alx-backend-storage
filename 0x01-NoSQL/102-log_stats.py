#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB, including the top 10 most present IPs.
"""

from pymongo import MongoClient

def log_stats():
    """
    Provides statistics about Nginx logs, including the top 10 most present IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    print("IPs:")
    pipeline = [
        { "$group": { "_id": "$ip", "count": { "$sum": 1 } } },
        { "$sort": { "count": -1 } },
        { "$limit": 10 }
    ]
    for ip_stat in collection.aggregate(pipeline):
        print(f"\t{ip_stat['_id']}: {ip_stat['count']}")

if __name__ == "__main__":
    log_stats()

