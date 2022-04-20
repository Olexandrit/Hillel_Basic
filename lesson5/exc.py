fruits = ['apple', 'banane', 'lemon', 'other']

try:

    my_fruit = fruits[10]
    print(my_fruit)

except IndexError:
    print('no')
finally:
    print('yes')
