""" a script that takes in arguments and displays
all values in the states table of
hbtn_0e_0_usa where name matches the
argument. But this time, write one
that is safe from MySQL injections!
"""
if __name__ == "__main__":
    # importing modules mysql db & sys
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    connector = MySQLdb.connect(user=username, passwd=password, db=database)
    # a cursor to manipulate the database
    db_cur = connector.cursor()

    state_search = sys.argv[4]
    query = "SELECT * FROM states \
        WHERE name = %(state_key)s"
    db_cur.execute(query, {'state_key': state_search})
    states_data = db_cur.fetchall()
for data in states_data:
    print(data)
    