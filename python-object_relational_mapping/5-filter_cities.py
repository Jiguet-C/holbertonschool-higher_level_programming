#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cities = []
    cur = db.cursor()
    if len(argv) == 5:
        cur.execute("""SELECT cities.name FROM states\
        INNER JOIN cities ON states.id = cities.state_id\
        WHERE states.name = % s\
        ORDER BY cities.id""", (argv[4],))

        rows = cur.fetchall()
        for row in rows:
            cities.append(row[0])
    print("{}".format(', '.join(cities)))
    cur.close()
    db.close()
