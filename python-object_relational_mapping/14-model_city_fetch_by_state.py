#!/usr/bin/python3
"""
A script 14-model_city_fetch_by_state.py
that prints all City objects from the database
hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in res:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
