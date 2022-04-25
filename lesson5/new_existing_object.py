fruits = ['🍊', '🍏', '🍌', '🍉', '🍋', '🍑']
smoothie = fruits
smoothie.remove('🍏')
smoothie.remove('🍉')
smoothie.remove('🍋')

print(smoothie)  # ['🍊', '🍌', '🍑']
print(fruits)  # ['🍊', '🍌', '🍑']
print(smoothie == fruits)  # True
print(smoothie is fruits)  # True

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
b = a
print(a is b)  # True

fruits = ['🍊', '🍏', '🍌', '🍉', '🍋', '🍑']
smoothie = fruits.copy()
smoothie = fruits[::]  # результат той самий
smoothie.remove('🍏')
smoothie.remove('🍉')
smoothie.remove('🍋')

print(smoothie)  # ['🍊', '🍌', '🍑']
print(fruits)  # ['🍊', '🍏', '🍌', '🍉', '🍋', '🍑']
print(smoothie == fruits)  # False
print(smoothie is fruits)  # False