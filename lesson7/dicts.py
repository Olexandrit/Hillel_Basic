# словник = {ключ: значення}
fruits = {'orange': '🍊', 'banana': '🍌'}
print(fruits)

print(fruits['orange'])
print(fruits['banana'])
# print(fruits['cucumber'])  # KeyError
print(fruits.get('cucumber'))  # якщо такого ключа немає, поверне None
print(fruits.get('banana'))
print(fruits.get('cucumber', '📦'))  # якщо такого ключа немає, поверне '📦'
print(fruits.get('banana', '📦'))

# Чому не варто завжди використовувати get
values = {
    'name': 'Тарас',
    # 'birth_year': 1990,  # забули вказати потрібний ключ
}
# print('Привіт,', values['name'], 'тобі', 2022 - values['birth_year'], 'роки')
# print('Привіт,', values.get('name'), 'тобі', 2022 - values.get('birth_year'), 'роки')

# додаємо елементи в словник:
fruits['pear'] = '🥒'
print(fruits)
fruits['pear'] = '🍐'
print(fruits)

# трошки магії 🦄
magic = {}  # так можна створити пустий dict
magic = dict()  # і так можна
magic[print] = 'OMG!'  # функція може бути ключем 😱
print(magic[print])

# ключі унікальні та immutable, значення - будь-які
fruits = {'orange': '🍊', 'orange': 'апельсин'}  # залишиться лише один, останній
print(fruits)
fruits = {'orange': '🍊', 'апельсин': '🍊'}  # значення можуть бути будь-які
print(fruits)
# no = {[1, 2, 3]: '123'}  # ключами можуть бути тільки незмінні типи данних (immutable)
yes = {(1, 2, 3): '123'}  # а tuple то immutable
print(yes)
yes = {'123': [1, 2, 3]}  # значення, все ще, можуть бути будь-які
print(yes)

# операції з dict
fruits = {'orange': '🍊', 'banana': '🍌'}
print('orange' in fruits)  # перевірка чи є ключ в словнику
print(len(fruits))  # кількість елементів в словнику

del fruits['banana']  # видалення елементу
print(fruits)
fruits.clear()  # очистити (видалити все)
print(fruits)

fruits = {'orange': '🍊', 'banana': '🍌'}
print(fruits.pop('banana'))  # "витягнути" елемент зі списку
print(fruits)

fruits = {'orange': '🍊', 'banana': '🍌'}
more_fruits = {'kiwi': '🥝', 'apple': '🍏', 'banana': '🍌🍌'}
fruits.update(more_fruits)  # додати один словник в інший
print(fruits)  # якщо ключ був - він отримає нове значення, якщо не було - буде створений