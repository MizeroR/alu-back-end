#!/usr/bin/python3
"""gathering all data"""
import requests
import sys


if __name__ == "__main__":
    #  URL of JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    total_number_of_tasks = requests/
    .get(url + "total_number_of_tasks", params).json()

    # Filter completed tasks and count them
    number_of_done_tasks = [t.get("title") for t in total_number_of_tasks if t.get("number_of_done_tasks") is True]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("employee_name"), len(number_of_done_tasks), len(total_number_of_tasks)))

    # Print the completed tasks one by one with indentation
    [print("\t {}".format(complete)) for complete in number_of_done_tasks]
