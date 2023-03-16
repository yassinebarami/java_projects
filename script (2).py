import json
json_str = '{"one": 1, "two": 2, "three": 3}'
json_obj = json.loads(json_str)

with open('data.json', 'w') as f:
	json.dump(json_obj, f, indent=2)

'''
data.json:

{
	"one": 1,
	"two": 2,
	"three": 3
}
'''
