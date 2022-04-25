fruits = ('🍑', '🍌', '🍏')
default_fruit = '🍊'

try:
    my_fruit = fruits[3]
except IndexError:
    my_fruit = default_fruit
finally:
    print('Yo!')

print(my_fruit)