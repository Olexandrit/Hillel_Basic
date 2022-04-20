empty_list = []
print(type(empty_list))
empty_list = list()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# індекси: 0  1  2  3  4  5  6  7  8  9
print(numbers[0])
print(numbers[3])
print(numbers[4:8])

stuff = [23, 2.5, 'cucumber', True, True, None,
         [1, 2, 3]]  # в список можна пхати будь що
print(stuff)
print(stuff[0] * stuff[1])

ducks = ['Hanry', 'Quacker']
new_ducks = ['Lupa', 'Pupa']
my_ducks = ducks + new_ducks
print(my_ducks)
print(my_ducks * 2)

my_ducks = my_ducks + 'Rose'  # ні
my_ducks = my_ducks + ['Rose']  # так

my_ducks.append('Rose')
print(my_ducks)
print(len(my_ducks))  # довжина списку (кількість елементів)
print(my_ducks.index('Lupa'))

my_ducks.append('Lupa')
print(my_ducks)
print(my_ducks.count('Lupa'))
my_ducks.remove('Lupa')
print(my_ducks)
del my_ducks[-1]
print(my_ducks)

my_ducks.insert(0, 'Wilhelm')
print(my_ducks)

# цикл for працює так само зі списками
digits = [1, 2, 3, 7, 8, 7, 2, 3, 0]
for digit in digits:
    if digit < 5:
        print(digit)
