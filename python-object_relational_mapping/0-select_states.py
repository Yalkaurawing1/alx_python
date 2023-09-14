#!/usr/bin/python3
# This script lists all states from the database hbtn_0e_0_usa

# Import the MySQLdb module
import MySQLdb

# Get the arguments from the command line
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server on localhost at port 3306
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=hbtn_0e_0_usa)

# Create a cursor object to execute queries
cur = db.cursor()

# Execute a query to select all states from the states table
cur.execute("SELECT * FROM states ORDER BY states.id ASC")

# Fetch all the results as a list of tuples
rows = cur.fetchall()

# Loop through each row and print it
for row in rows:
    print(row)

# Close the cursor and the database connection
cur.close()
db.close()
