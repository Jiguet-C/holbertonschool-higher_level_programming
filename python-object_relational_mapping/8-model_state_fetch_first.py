#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}".format(first_state.id) + ": " + "{}".
              format(first_state.name))
    else:
        print("Nothing")

    session.close()
