#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database"
              .format(sys.argv[0]))
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

    try:
        # Retrieve the State object with id 2
        state = session.query(State).filter(State.id == 2).first()

        if state:
            # Update the name of the state
            state.name = "New Mexico"
            session.commit()
            print("State updated successfully")
        else:
            print("State with id 2 not found")
    except Exception as e:
        print("Error occurred:", e)
        session.rollback()
    finally:
        # Close the session
        session.close()
