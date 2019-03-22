import requests
url = "http://api.open-notify.org/astros.json"
json_data = requests.get(url).json()
print (json_data["number"])
i = 0
while i < json_data["number"]:

        print (json_data["people"][i]["name"])
        i +=1