#Formar un json de un diccionario en python
import json
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)
# Output: ['English', 'French']
print(person_dict['languages'])

#fuente: https://www.programiz.com/python-programming/json