import pytest
import requests
import json

response = requests.get("https://reqres.in/api/users/2").json()
username = response['data']['first_name'] + " " + response['data']['last_name']

sourcefile = open("TestData.json", "r")
filedata = json.load(sourcefile)
Assert_Username = filedata['data']['first_name'] + " " + filedata['data']['last_name']


assert username == Assert_Username, "Username Retrieved is not matching the expected one"
print "Test Case Passed"






