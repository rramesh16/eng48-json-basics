import json

car_dictionary = {
    'name':'tesla',
    'engine':'90000kw',
    'type':'electric'
}

print(type(car_dictionary))
print(car_dictionary)

# json.dumps(dict_object) --> outputs a string
        # use this create JSON string from our dictionaries on the go
car_data_json_string = json.dumps(car_dictionary)
print(car_data_json_string)
print(type(car_data_json_string))

# json.dump(dict_object, file) --> writes JSON to a file

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_dictionary, jsonfile)

# json.load(jsonfile) --> outputs the dictionary
with open('new_json_file.json', 'r') as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car['engine'])