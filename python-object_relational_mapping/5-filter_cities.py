#!/usr/bin/python3
"""
A script that takes in the name of
a state as an argument and lists
all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database_name> <state_name>"
            .format(sys.argv[0])
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = db.cursor()
        # Use of query parameters
        cursor.execute(
            """
            SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE BINARY states.name=%s
            ORDER BY cities.id ASC
            """, (state_name,)
        )

        cities = cursor.fetchall()
        for x in range(len(cities)):
            if(x):
                print(", ", end="")
            print(cities[x][1], end="")
        print()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
