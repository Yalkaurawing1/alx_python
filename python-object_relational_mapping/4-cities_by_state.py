#!/usr/bin/python3
# This script lists all cities from the database hbtn_0e_4_usa
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    connector = MySQLdb.connect(user=username, passwd=password, db=database)

    # a cursor to manipulate the database
    db_cur = connector.cursor()
    db_cur.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities, states \
                   WHERE states.id = state_id ORDER BY cities.id")
    states_data = db_cur.fetchall()

for data in states_data:
    print(data)