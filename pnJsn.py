import json

employee = '{"name": "Baljeet", "age": 35, "address": {"city": "Vancouver", "country": "Canada"}, "skills": ["Python", "QA", "API Testing"]}'
employee_dict = json.loads(employee)
print(f"Name: {employee_dict['name']}")
print(f"City: {employee_dict['address']['city']}")
print(f"Country: {employee_dict['address']['country']}")
print(f"First Skill: {employee_dict['skills'][0]}")
print(f"Total Skills: {len(employee_dict['skills'])}")
