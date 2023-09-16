#!/usr/bin/python3
"""This script takes in an argument
and displays all values in the states
table of hbtn_0e_0_usa where name matches
the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    connector = MySQLdb.connect(user=username, passwd=password, db=database)

    # a cursor to manipulate the database
    cur = connector.cursor()

    cur.execute("USE test_2")
    state_search = sys.argv[4]
    query = "SELECT * FROM states \
            WHERE name COLLATE utf8mb4_bin LIKE '{}%'".format(state_search)
    cur.execute(query)
    states_data = cur.fetchall()

for data in states_data:
    print(data)