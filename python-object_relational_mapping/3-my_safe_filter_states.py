""" 
a script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

"""

import MySQLdb
import sys


def safe_query(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # Prepare the query with placeholders (%s) for safety
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the query with the provided arguments
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)


# Check if the script is not being imported
if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) == 6:
        # Call the safe_query function with the arguments
        safe_query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(
            "Please provide the required arguments: MySQL username, MySQL password, database name, and state name to be searched."
        )