#!/usr/bin/env python3
import MySQLdb
import sys

def list_states(username, password, db_name):
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Loop through the rows and print them
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # List all states from the database
    list_states(username, password, db_name)
