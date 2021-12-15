
import datetime
now = datetime.datetime.now()
print(now.year)

import time
time.sleep(1)

############################################

records = ["1", "2", "3"]
for record in records:
    print(record)

count = 2
while(count > 0):
    print("counting..")
    count = count-1

# Syntactically, there is no difference on lists:
cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
first_three = cities[0:3]
print(first_three)

############################################

import json
jsonString = """[
    {
        "Name": "Alex",
        "Age": "21"
    },
    {
        "Name": "Tina",
        "Age": "20"
    }
]"""
#print(jsonString)
jsonObject = json.loads(jsonString)
print(jsonObject[0]["Name"])
jsonString = json.dumps(jsonObject)

############################################


