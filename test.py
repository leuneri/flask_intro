import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 00, "name": "Vid0", "views": 20000},
        {"likes": 10, "name": "Vid1", "views": 21000},
        {"likes": 20, "name": "Vid2", "views": 22000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())