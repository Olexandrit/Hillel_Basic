import json

person_json = '''
{
  "first_name": "Rowney",
  "last_name": "Sivills",
  "email": "hsivills3@toplist.cz",
  "phones": [
    "+66 (483) 371-5390",
    "+98 (759) 391-3486",
    "+86 (673) 612-8409"
  ],
  "animal": {
    "type": "Salmon pink bird eater tarantula",
    "name": "Hephzibah"
  }
}
'''

person = json.loads(person_json)  # load(s) - load from (s)tring
print(type(person))
print(f"{person['first_name']} owns {person['animal']['name']}")

fruits = [
    {
        'icon': '🍏',
        'name': 'Apple',
        'nutrition': {
            'calories': 52,
            'water': 0.86,
            'protein': 0.3,
            'carbs': 13.8,
            'sugar': 10.4,
        },
    },
    {
        'icon': '🍌',
        'name': 'Banana',
        'nutrition': {
            'calories': 89,
            'water': 0.75,
            'protein': 1.1,
            'carbs': 22.8,
            'sugar': 12.2,
        },
    },
    {
        'icon': '🍓',
        'name': 'Strawberry',
        'nutrition': {
            'calories': 33,
            'water': 0.75,
            'protein': 1,
            'carbs': 12.7,
            'sugar': 7.4,
        },
    },
]

fruits_json = json.dumps(fruits)  # dump(s) - dump to (s)tring

print(type(fruits_json))
print(fruits_json)


with open('fruits.json', 'w') as json_file:
    json.dump(fruits, json_file)  # dump - dump to file


with open('fruits.json') as jsonfile:
    json_data = json.load(jsonfile)  # load - load from file
    print(type(json_data))
    print(json_data)
    print(len(json_data))

    for fruit in json_data:
        print(
            f"{fruit['icon']} {fruit['name']} is on {fruit['nutrition']['water'] * 100}% water"
        )
