#!/usr/bin/python3
"""Module listing all states with a name that matc the arg from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=argv[1],
          passwd=argv[2],
          db=argv[3]
          )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Create the SQL query to select states with the name matching the argument
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the SQL query with parameterized input to prevent SQL injection
    cur.execute(query, (argv[4],))

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
