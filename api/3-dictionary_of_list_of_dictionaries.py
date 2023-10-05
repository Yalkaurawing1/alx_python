#!/usr/bin/python3
"""
This module uses a REST API to get information about all employees' TODO list progress and export it in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/users/"
    # Get the list of all employees from the API
    employees = requests.get(base_url).json()
    # Create a dictionary to store the records of tasks for all employees
    records = {}
    # Loop through the employees list and get the details and TODO list for each employee
    for employee in employees:
        # Get the employee ID, name and username from the details
        employee_id = employee.get("id")
        employee_name = employee.get("name")
        employee_username = employee.get("username")
        # Get the employee TODO list from the API
        todos = requests.get(base_url + str(employee_id) + "/todos").json()
        # Create a list to store the tasks as dictionaries
        tasks = []
        # Loop through the TODO list and create a task dictionary for each task
        for todo in todos:
            # Get the task completed status and title from the task
            task_completed = todo.get("completed")
            task_title = todo.get("title")
            # Create a task dictionary with these keys and values: username, task, completed
            task = {"username": employee_username, "task": task_title, "completed": task_completed}
            # Append the task dictionary to the tasks list
            tasks.append(task)
        # Assign the tasks list as the value of the employee ID key in the records dictionary
        records[employee_id] = tasks
    # Define the file name as todo_all_employees.json
    file_name = "todo_all_employees.json"
    # Open the file in write mode
    with open(file_name, "w") as file:
        # Dump the records dictionary to the file as a JSON string
        json.dump(records, file)
