import json

person = '{"name": "Baljeet", "age": 35, "city": "Vancouver"}'
person_dict = json.loads(person)
print(f"Name: {person_dict['name']}")
print(f"Age: {person_dict['age']}")
print(f"City: {person_dict['city']}")