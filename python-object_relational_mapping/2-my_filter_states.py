#!/usr/bin/python3
"""
A script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
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
        cursor.execute(
            """
            SELECT * FROM states
                WHERE BINARY name=%s
            ORDER BY id ASC
            """, (state_name,)
        )

        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
