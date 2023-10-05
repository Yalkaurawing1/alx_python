#!/usr/bin/python3

#!/usr/bin/python3
"""
This module uses a REST API to get information about an employee's TODO list progress.
"""

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
        # Get the employee name from the details
        employee_name = employee.get("name")
        # Get the employee TODO list from the API
        todos = requests.get(base_url + employee_id + "/todos").json()
        # Count the total number of tasks and the number of done tasks
        total_tasks = len(todos)
        done_tasks = 0
        # Create a list to store the titles of completed tasks
        done_titles = []
        # Loop through the TODO list and check the status of each task
        for todo in todos:
            # If the task is completed, increment the done_tasks counter and append the title to the done_titles list
            if todo.get("completed"):
                done_tasks += 1
                done_titles.append(todo.get("title"))
        # Display the employee TODO list progress on the standard output
        print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
        # Loop through the done_titles list and display each title with a tabulation and a space before it
        for title in done_titles:
            print("\t {}".format(title))
    else:
        # If the script does not receive an integer as a parameter, print an error message and exit
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
        sys.exit(1)
