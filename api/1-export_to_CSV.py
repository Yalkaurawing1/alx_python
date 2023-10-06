"""
This script uses an API to retrieve employee task information
and display in a special format.

It retrieves employees name, task completed with their titles.
"""
import csv
import requests
import sys

# No execution of this file when imported
if __name__ == "__main__":
    
# Pass employee id on command line
    id = sys.argv[1]

# APIs 
    userTodoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(id)

# Make requests on APIs
    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

# Parse responses and store in variables
    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

#Get employee information
    employeeName = profileJson_Data['username']

    dataList = []

    for data in todoJson_Data:
        dataDict = {"userId":data['userId'], "name":employeeName, "completed":data['completed'], "title":data['title']}
        dataList.append(dataDict)

    # Specify the CSV file path
    csv_file_path = '{}.csv'.format(todoJson_Data[0]['userId'])

    # Define the field names (column headers)
    fieldnames = ["userId", "name", "completed", "title"]

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        # Write the data rows
        for row in dataList:
            csv_writer.writerow(row)