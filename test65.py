import requests

test= requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
response=test.json()
for i in range(len(response)):
   print(response[i]["user"]["login"])


test1=[{"name": "siva","age":"33"},{"name": "siva","age":"33"}]

for i in range(len(test1)):
    for key,value in test1[i].items():
        print(key,value)
