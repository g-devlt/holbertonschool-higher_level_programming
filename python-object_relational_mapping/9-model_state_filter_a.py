#!/usr/bin/python3
"""
A script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine, asc
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

    res = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(asc(State.id))
        .all()
    )

    for state in res:
        print(f"{state.id}: {state.name}")

    session.close()
