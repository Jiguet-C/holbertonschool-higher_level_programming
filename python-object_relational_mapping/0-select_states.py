#!/usr/bin/python3
"""Module listing all states from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=argv[1],
          passwd=argv[2],
          db=argv[3],
          )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states ordered by their ID
    cur.execute("""SELECT * FROM states ORDER BY id""")

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
