#!/usr/bin/python3
# This script takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument

# Import the MySQLdb module and the sys module
import MySQLdb
import sys

# Get the arguments from the command line
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Connect to the MySQL server on localhost at port 3306
connector = MySQLdb.connect(user=username, passwd=password, db=database)

# Create a cursor object to execute queries
cur = connector.cursor()

cur.execute("USE test_2")

# Use format to create the SQL query with the user input
query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id ASC".format(state_name)

# Execute the query
cur.execute(query)

# Fetch all the results as a list of tuples
state_name = cur.fetchall()

# Loop through each row and print it
for state in states_name:
    print(state)

# Close the cursor and the database connection
cur.close()
connector.close()
