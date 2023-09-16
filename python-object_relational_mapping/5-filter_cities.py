"""a script that takes in the name of
a state as an argument and lists all
cities of that state, using the
database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]

    # Connect to the database
    connector = MySQLdb.connect(user=username, passwd=password, db=database)

    # a cursor to manipulate the database
    cursor = connector.cursor()
    cursor.execute("""SELECT name
                   FROM cities
                   WHERE state_id =
                    (SELECT id FROM states
                    WHERE name COLLATE utf8mb4_bin LIKE '{}%')
                   ORDER BY id ASC""".format(state_searched))
    states_data = cursor.fetchall()

    cities = ', '.join(data[0] for data in states_data)
    print(cities)
