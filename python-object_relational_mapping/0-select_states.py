#!/usr/bin/python3
# This script lists all states from the database hbtn_0e_0_usa

# if name = main
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    connector = MySQLdb.connect(user=user, passwd=password, db=database)

    # a cursor to manipulate the database
    db_cur = connector.cursor()

    db_cur.execute("SELECT * FROM states")
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)