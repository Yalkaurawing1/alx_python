# Import requests module
import requests

# Define the base URL for the REST API
base_url = "https://jsonplaceholder.typicode.com/users/"

# Get the employee ID from the user input
employee_id = int(input("Enter the employee ID: "))

# Construct the URL for the employee details and TODO items
employee_url = base_url + str(employee_id)
todo_url = base_url + str(employee_id) + "/todos"

# Get the JSON response from the API
employee_response = requests.get(employee_url).json()
todo_response = requests.get(todo_url).json()

# Get the employee name from the response
employee_name = employee_response["name"]

# Initialize the variables for counting the tasks
total_tasks = 0
done_tasks = 0

# Loop through the TODO items and count the completed tasks
for item in todo_response:
    total_tasks += 1
    if item["completed"]:
        done_tasks += 1

# Print the first line of the output
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

# Loop through the TODO items again and print the title of completed tasks
for item in todo_response:
    if item["completed"]:
        print(f"\t {item['title']}")
