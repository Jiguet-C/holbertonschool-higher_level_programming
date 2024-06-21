#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()
    Base.metadata.create_all(engine)

    # Query for State objects containing the letter 'a', sorted by id
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id.asc())

    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
