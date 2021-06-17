import json

dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {"key1": "value1", "key2": "value2"}

print(json.dumps(dict1))
print(str(dict1))

print(json.dumps(dict2))
print(str(dict2))
