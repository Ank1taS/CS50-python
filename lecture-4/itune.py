import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# returned value of requests.get will be stored in response
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
)

"""
# json.dumps is implemented such that it utilizes indent to make the output more readable
print(response.json())


# the JSON response is converted by Python into a dictionary. Looking at the output,
print(json.dumps(response.json(), indent=2))
"""


# result of response.json() and storing it in o (as in the lowercase letter). Then, we are iterating through the results in o and printing each trackName
o = response.json()
for results in o["results"]:
    print(results["trackName"])
