#!/usr/bin/python3
"""
A script that changes the name of
a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database>"
            .format(sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # As per the requirement,
    # fetching the State object with id=2
    state = (
        session.query(State)
        .filter(State.id == 2)
        .first()
    )

    if state is not None:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State not found")

    session.close()
