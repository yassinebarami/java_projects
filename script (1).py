import json

json_obj = json.loads('{"one": 1, "two": 2, "three": 3}')

with open('data.json', 'w') as f:
	json.dump(json_obj, f)

'''
data.json:

{"one": 1, "two": 2, "three": 3}

'''
