#!/usr/bin/python3
"""
This module uses a REST API to get information
about an employee's TODO list progress
and export it in the CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the script receives an integer as a parameter
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        # Get the employee ID from the parameter
        employee_id = sys.argv[1]
        # Define the base URL for the API
        base_url = "https://jsonplaceholder.typicode.com/users/"
        # Get the employee details from the API
        employee = requests.get(base_url + employee_id).json()
        # Get the employee name and username from the details
        employee_name = employee.get("name")
        employee_username = employee.get("username")
        # Get the employee TODO list from the API
        todos = requests.get(base_url + employee_id + "/todos").json()
        # Create a list to store the records of tasks that are owned by this employee
        records = []
        # Loop through the TODO list and create a record for each task
        for todo in todos:
            # Get the task completed status and title from the task
            task_completed = todo.get("completed")
            task_title = todo.get("title")
            # Create a record as a list of values in this order: user ID, username, task completed status, task title
            record = [employee_id, employee_username, task_completed, task_title]
            # Append the record to the records list
            records.append(record)
        # Define the file name as USER_ID.csv
        file_name = employee_id + ".csv"
        # Open the file in write mode
        with open(file_name, "w") as file:
            # Create a csv writer object
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            # Loop through the records list and write each record to the file
            for record in records:
                writer.writerow(record)
    else:
        # If the script does not receive an integer as a parameter, print an error message and exit
        print("Usage: ./1-export_to_CSV.py <employee ID>")
        sys.exit(1)
