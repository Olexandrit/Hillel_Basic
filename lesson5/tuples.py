empty_tuple = ()
print(type(empty_tuple))
empty_tuple = tuple()

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[0])
print(numbers[3])
print(numbers[4:8])

stuff = (23, 2.5, 'cucumber', True, True, None, [1, 2, 3])
print(stuff)
print(stuff[0] * stuff[1])

ducks = ('Hanry', 'Quacker')
new_ducks = ('Lupa', 'Pupa')
my_ducks = ducks + new_ducks
print(my_ducks)
print(my_ducks * 2)

# my_ducks.append('Rose')  # в існуючій кортеж не можна додати елемент
# print(my_ducks)

print(my_ducks.index('Quacker'))
print(my_ducks.count('Lupa'))

fruits = ('🍊', '🍏', '🍌', '🍉', '🍋', '🍑')
smoothie = fruits
smoothie = fruits[0:1] + fruits[2:3] + fruits[5:6]
smoothie = (fruits[0], fruits[2], fruits[5])
# smoothie.remove('🍏')   # з існуючого кортежу не можна прибрати елемент
# smoothie.remove('🍉')
# smoothie.remove('🍋')

print(smoothie)
print(fruits)
print(smoothie == fruits)
print(smoothie is fruits)

# довжина кортежу
len(smoothie)

# приклад
print('Розпізнавач фруктів 3000')
fruits = ('🍊', '🍏', '🍌', '🍉', '🍋', '🍑')
item = input('Що розпізнати? ')

if item in fruits:
    print(f'{item} це фрукт!')
else:
    print(f'{item} це не фрукт!')