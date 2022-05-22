ducks = open('ducks.txt')
print(ducks)
print(ducks.read())
# 1/0  # якщо станеться помилка, файл не буде закрито як подобає
ducks.close()  # тому так краще не робити


# краще так:
with open('ducks.txt') as ducks:
    print(ducks.read())
# print(ducks.read())  # помилка "I/O operation on closed file"


with open('ducks.txt', 'r') as ducks:  # 'r' - read відкрити файл для зчитування, це значення за замовчуванням
    print(ducks.read())    
    print(ducks.read())  # нічого
    ducks.seek(0)  # переносимо курсор на початок файлу
    print(ducks.read())  # знову виведе


gin_sour = '''Gin Sour:
- 2 oz Gin
- 3/4 oz Lemon Juice
- 3/4 oz Simple syrup
'''

with open('gin_sour.txt', 'w') as recipe:  # 'w' - write відкрити файл для запису
    recipe.write(gin_sour)


gin_sour = '''Gin Sour:
- 2 oz Gin
- 3/4 oz Lemon Juice
- 3/4 oz Simple syrup

Shake and serve
'''

with open('gin_sour.txt', 'w') as recipe:
    recipe.write(gin_sour)  # замінить існуючий у файлі текст


gin_sour_parts = [
    '2 oz Gin\n',
    '3/4 oz Lemon Juice\n',
    '3/4 oz Simple syrup\n',
]

with open('gin_sour.txt', 'w') as recipe:
    recipe.write('Gin Sour:\n')
    
with open('gin_sour.txt', 'a') as recipe:  # 'a' - append відкрити файл для запису з додаванням в кінці файлу
    for part in gin_sour_parts:
        recipe.write(part)

with open('gin_sour.txt', 'a') as recipe:
    recipe.writelines(gin_sour_parts)
    # print(recipe.read())  # помилка бо файл відкрит для запису

with open('gin_sour.txt') as recipe:  # без вказання режиму, файл відкривається для запису
    print(recipe.readlines())
    # recipe.write('Shake and serve')  # помилка бо файл відкрит для зчитування
    

import io
from pathlib import Path


recipe_path = Path('gin_sour.txt')


with open(recipe_path, 'r+') as recipe:  # 'r+' - зчитування та запис
    recipe.write('Shake and serve')  # буде додано на початку файлу
    recipe.seek(0)
    print(recipe.read())
    recipe.seek(0, io.SEEK_END)  # перенести курсор на кінець файлу (0 байтів від кінця файлу)
    recipe.write('Shake and serve')  # буде додано в кінець файлу
    recipe.seek(0, io.SEEK_SET)  # також перенести курсор на початок файлу (0 байтів від початку файлу)
    print(recipe.read())


recipe_path.unlink()  # видалити файл

# існує також режим `b` - бінарний, для зчитування ('rb') або запису ('wb') байтів файлу. 
# Наприклад для роботи з зображеннями

with open('ducks.txt', 'rb') as ducks:
    content = ducks.read()

with open('new_ducks.txt', 'wb') as ducks:
    ducks.write(content)
    
# в результаті отримаємо такий самий файл з іншою назвою
