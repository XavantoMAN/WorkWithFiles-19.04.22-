import json
f = open('1.json')
data = json.load(f)
print(data['name'])
f.close()
