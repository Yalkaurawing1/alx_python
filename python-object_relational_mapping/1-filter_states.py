'''
Write a script that lists all states with a
name starting with N (upper N) from the database hbtn_0e_0_usa:
'''
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

    query = "SELECT * FROM states \
                   WHERE name COLLATE utf8mb4_bin LIKE 'N%'"
    db_cur.execute(query)
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)
