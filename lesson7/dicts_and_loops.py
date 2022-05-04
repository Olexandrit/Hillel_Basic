fruits = {
    'orange': '🍊',
    'banana': '🍌',
    'kiwi': '🥝',
    'apple': '🍏',
}

for fruit in fruits:  # так будуть тільки ключі
    print(fruit)

for fruit in fruits.keys():  # так теж тільки ключі
    print(fruit)

for fruit in fruits:
    print(fruits[fruit])  # по ключу можна отримати значення

for fruit in fruits.values():  # так будуть тільки значення
    print(fruit)

for fruit in fruits.items():  # так будуть і ключі і значення у tuple
    print(fruit)

for name, emoji in fruits.items():  # але так зручніше
    print(f'{emoji} це {name}')

# також можна перетворити у список або кортеж
print(list(fruits.keys()))
print(list(fruits.values()))
print(list(fruits.items()))  # отримаємо список таплів

print(set(fruits.values()))  # в сет також можна

# Загальне правило, якщо це можна використати (ітерувати) в циклі for, то можна і перетворити у list, tuple або set
# Тому строки також можна
print(list('cucumber'))