import json
import pprint

with open('data.json', 'r') as f:
	data = f.read()
	json_data = json.loads(data)

print(json_data)
