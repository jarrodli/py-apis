# jarrod li
# attempting to use the requests module
# to play around with api requests

import requests, json

parameters = {"lat": 33.87, "lon": 151.2}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# print(response.content)

# convert .json format strings to python dict objects

data = response.json()
print(type(data))
print(data)

# headers is a dictonary
print(response.headers)

# get content type
print(response.headers["content-type"])

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

print(data["number"])
print(data)