is_odd = lambda num: num % 2 == 1
print(is_odd(3))
print(is_odd(2))

letters_and_numbers = {'a': 23, 'c': 18, 'b': 20, 'd': 33}

print(dict(sorted(letters_and_numbers.items(), key=lambda item: item[1])))

add = lambda x, y, z: x + y + z
print(add(1, 2, 3))

hi = lambda: print('Hi')
hi()

say = lambda what: print('Simon says', what)
say('cucumber')

printer = lambda *args: print('\n'.join(args))
printer('hello', 'cucumber', 'abc')

# lambda: variable = 123  # не можна створити змінну в лямбді
