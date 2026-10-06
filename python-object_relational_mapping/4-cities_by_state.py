#!/usr/bin/python3
"""
A script that lists all cities
from the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <database_name>"
            .format(sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
        )

        cities = cursor.fetchall()
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
