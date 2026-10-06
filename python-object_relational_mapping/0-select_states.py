#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states from the 'states' table,
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute the SQL query to retrieve all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all results and print them
        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()