numbers = [54, 6, 50, 46, 0, 94, 2, 91, 89, 14]
print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))

print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(sorted('cucumbers'))

letters_and_numbers = {'a': 23, 'c': 18, 'b': 20, 'd': 33}

print(dict(sorted(letters_and_numbers.items())))

def sort_by_value(item):
    return item[1]

print(dict(sorted(letters_and_numbers.items(), key=sort_by_value)))


ducks = [
    'Hanry',
    'Alexis',
    'Rose',
    'Lupa',
    'Julianna',
    'Quacker',
]

print(sorted(ducks))
print(sorted(ducks, key=len))

wierdo = ['cucumber', 23, 5.7, True]
print(sorted(wierdo))  # помилка, неможливо порівняти str та int
