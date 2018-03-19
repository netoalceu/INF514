import json
 
# you can also use the open function to read the content of a JSON file to a string
json_data = """ {
    "key 1": "value 1",
    "key 2": "value 2",
    "decimal": 10,
    "boolean": true,
    "list": [1, 2, 3],
    "dictionary": {
        "child key 1": "child value",
        "child key 1": "child value"
    }
}"""
 
my_dict = json.loads(json_data)

#print("string value: %s" % my_dict["key 1"])
#print("decimal value: %d" % my_dict["decimal"])
#print("decimal value: %r" % my_dict["boolean"])
#print("list values: %s" % my_dict["list"])

my_dictionary = {
    "key 1": "Value 1",
    "key 2": "Value 2",
    "decimal": 100,
    "boolean": False,
    "list": [1, 2, 3],
    "dict": {
        "child key 1": "value 1",
        "child key 2": "value 2"
    }
}

print(json.dumps(my_dictionary))
print(json.dumps(my_dictionary, indent=4))


