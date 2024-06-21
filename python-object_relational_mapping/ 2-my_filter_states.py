#!/usr/bin/python3
"""Module listing all states with a name that matc the arg from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query with parameterized input
    cur.execute(
        """SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"""
        .format(argv[4]))
    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
