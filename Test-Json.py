import json

with open("Test-Json.json", "r") as read_file:
    data = json.load(read_file)

dic_data = {}
for x in data.values():
    dic_data[str(x["name"])] = (int(x["score"]))

i = 1
data = {}
for x,y in dic_data.items() :
    z = "player"
    z += " " + str(i)
    data[z]={"name" : x, "score" : str(y)}
    i += 1

with open("Test-Json.json", "w") as write_file:
    json.dump(data, write_file)

print(dic_data)