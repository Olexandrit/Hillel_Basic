# pip install requests

import requests


# GET запит
response = requests.get('https://example.com')
print(response)
print(response.status_code)
print(response.text)  # тіло відповіді

# відповідь у вігляді JSON
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
data = response.json()
print(data)
print(
    'Міжнародна космічна станція зараз над цими координатами:'
    f' {data["iss_position"]["latitude"]}, {data["iss_position"]["longitude"]}'
)

# POST запит
# створюємо першу нотатку
response = requests.post(
    'http://127.0.0.1:8000/notes/',
    json={'title': 'Hi', 'text': 'This is the first note'},
)
print(response.status_code)
first_note = response.json()
print(first_note)

# створюємо другу нотатку
response = requests.post(
    'http://127.0.0.1:8000/notes/',
    json={'title': 'Cucumber', 'text': 'This is the second note'},
)
print(response.status_code)
second_note = response.json()
print(second_note)

# отримуємо список нотаток
response = requests.get('http://127.0.0.1:8000/notes/')
print(response.json())

# PUT запит
# змінюємо другу нотатку
response = requests.put(
    f'http://127.0.0.1:8000/notes/{second_note["id"]}/',
    json={'title': 'Cucumber', 'text': 'This is a note about cucumber'},
)
print(response.status_code)

# отримуємо список нотаток (перевіряємо)
response = requests.get('http://127.0.0.1:8000/notes/')
print(response.json())

# DELETE запит
# видаляємо першу нотатку
response = requests.delete(f'http://127.0.0.1:8000/notes/{first_note["id"]}/')
print(response.status_code)
print(response.json())

# отримуємо список нотаток (перевіряємо)
response = requests.get('http://127.0.0.1:8000/notes/')
print(response.json())
