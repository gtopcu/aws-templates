
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

response = {} #dict
response['transactionId'] = 1000
response['type'] = "buy order"   
jsonResponse = json.dumps(response)

