#!/usr/bin/python3
# This script lists all cities from the database hbtn_0e_4_usa
if __name__ == "__main__":
    # Import the MySQLdb module
    import MySQLdb
    import sys
# Get the arguments from the command line
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server on localhost at port 3306
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Create a cursor object to execute queries
cur = db.cursor()

# Execute a query to select all cities from the cities table
cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")

# Fetch all the results as a list of tuples
rows = cur.fetchall()

# Loop through each row and print it
for row in rows:
    print(row)

# Close the cursor and the database connection
cur.close()
db.close()
