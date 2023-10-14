# Import json module
import json
# Import requests module
import requests
# Import sys module
import sys

# Get the employee ID from the command line argument
employee_id = sys.argv[1]

# Define the base URL for the API
base_url = "https://jsonplaceholder.typicode.com/users/"

# Get the employee details from the API
employee_response = requests.get(base_url + employee_id)
# Check if the response is valid
if employee_response.status_code == 200:
    # Parse the JSON data
    employee_data = employee_response.json()
    # Get the employee name
    employee_name = employee_data["name"]
    # Get the employee username
    employee_username = employee_data["username"]
    # Get the employee TODO list from the API
    todo_response = requests.get(base_url + employee_id + "/todos")
    # Check if the response is valid
    if todo_response.status_code == 200:
        # Parse the JSON data
        todo_data = todo_response.json()
        # Initialize an empty list for storing the tasks data
        tasks_data = []
        # Loop through the TODO list
        for task in todo_data:
            # Create a dictionary with the task title, completed status and username
            task_dict = {"task": task["title"], "completed": task["completed"], "username": employee_username}
            # Append the dictionary to the list of tasks data
            tasks_data.append(task_dict)
        # Create a dictionary with the employee ID and the tasks data
        export_data = {employee_id: tasks_data}
        # Define the file name for exporting the data
        file_name = employee_id + ".json"
        # Open the file in write mode
        with open(file_name, "w") as f:
            # Dump the export data to the file in JSON format
            json.dump(export_data, f)
        # Print a success message
        print("Data exported to {}".format(file_name))
    else:
        # Print an error message if the TODO response is invalid
        print("Error: Could not get the TODO list for employee {}".format(employee_id))
else:
    # Print an error message if the employee response is invalid
    print("Error: Could not get the details for employee {}".format(employee_id))
