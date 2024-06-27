#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "TOTAL_NUMBER_OF_TASKS", params={"userId": sys.argv[1]}).json()

    NUMBER_OF_DONE_TASKS = [t.get("title") for t in todos if t.get("NUMBER_OF_DONE_TASKS") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("EMPLOYEE_NAME"), len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
    [print("\t {}".format(c)) for c in NUMBER_OF_DONE_TASKS]