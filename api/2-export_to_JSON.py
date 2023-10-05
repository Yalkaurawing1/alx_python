#!/usr/bin/python3
"""
This module uses a REST API to get information about an employee's TODO list progress and export it in the JSON format.
"""

import json
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
        # Get the employee username from the details
        employee_username = employee.get("username")
        # Get the employee TODO list from the API
        todos = requests.get(base_url + employee_id + "/todos").json()
        # Create a dictionary to store the records of tasks that are owned by this employee
        records = {}
        # Create a list to store the tasks as dictionaries
        tasks = []
        # Loop through the TODO list and create a task dictionary for each task
        for todo in todos:
            # Get the task completed status and title from the task
            task_completed = todo.get("completed")
            task_title = todo.get("title")
            # Create a task dictionary with these keys and values: task, completed, username
            task = {"task": task_title, "completed": task_completed, "username": employee_username}
            # Append the task dictionary to the tasks list
            tasks.append(task)
        # Assign the tasks list as the value of the employee ID key in the records dictionary
        records[employee_id] = tasks
        # Define the file name as USER_ID.json
        file_name = employee_id + ".json"
        # Open the file in write mode
        with open(file_name, "w") as file:
            # Dump the records dictionary to the file as a JSON string
            json.dump(records, file)
    else:
        # If the script does not receive an integer as a parameter, print an error message and exit
        print("Usage: ./2-export_to_JSON.py <employee ID>")
        sys.exit(1)
