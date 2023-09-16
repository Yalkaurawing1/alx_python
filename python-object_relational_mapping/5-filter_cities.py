"""a script that takes in the name of
a state as an argument and lists all
cities of that state, using the
database hbtn_0e_4_usa
"""
import MySQLdb
import sys

def get_cities_by_state(username, password, database, state):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities
    cursor.execute("""SELECT name
                   FROM cities
                   WHERE state_id =
                    (SELECT id FROM states
                    WHERE name COLLATE utf8mb4_bin LIKE '{}%')
                   ORDER BY id ASC""".format(state))
    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == '__main__':
    # Get the command-line arguments
    username, password, database, state = sys.argv[1:]

    # Call the function to retrieve cities by state
    get_cities_by_state(username, password, database, state)
