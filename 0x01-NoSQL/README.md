# ALX Backend Storage

## 0x01-NoSQL

This project contains various scripts and functions for interacting with MongoDB, implemented using JavaScript and Python.

### Table of Contents

- [0. List all databases](#0-list-all-databases)
- [1. Create or use a database](#1-create-or-use-a-database)
- [2. Insert a document](#2-insert-a-document)
- [3. List all documents](#3-list-all-documents)
- [4. List documents by match](#4-list-documents-by-match)
- [5. Count documents](#5-count-documents)
- [6. Update documents](#6-update-documents)
- [7. Delete documents by match](#7-delete-documents-by-match)
- [8. List all documents in Python](#8-list-all-documents-in-python)
- [9. Insert a document in Python](#9-insert-a-document-in-python)
- [10. Update topics in Python](#10-update-topics-in-python)
- [11. Find schools by topic](#11-find-schools-by-topic)
- [12. Log stats in Python](#12-log-stats-in-python)
- [100. Find by regex](#100-find-by-regex)
- [101. Top students](#101-top-students)
- [102. Log stats with IPs](#102-log-stats-with-ips)

### 0. List all databases

This script lists all databases in MongoDB.

File: `0-list_databases`

```javascript
// my comment
db.adminCommand('listDatabases').databases.forEach(function(d) {
    print(d.name + "\t" + (d.sizeOnDisk / 1024 / 1024 / 1024).toFixed(3) + "GB");
});

