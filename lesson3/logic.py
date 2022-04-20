hanry_is_duck = True
quacker_is_duck = True
me_is_duck = False

print(hanry_is_duck and quacker_is_duck)
print(hanry_is_duck and me_is_duck)

print(hanry_is_duck or me_is_duck)
friend_is_duck = False
print(me_is_duck or friend_is_duck)

print(True and True)  # True
print(True and False)  # False
print(True or False)  # True
print(False or False)  # False
print(not False)  # True
print(not True)  # False

# Можна поєднувати
print(True and not False)
print(True and True and True and False)
print(True or False and True)

# Скобками можно групувати
print(True or False and False)  # True
print((True or False) and False)  # False

number = 5
print(number > 0 and number < 10)
print(0 < number < 10)  # скорочений варіант
print(number == 5 or number == 10)

text = 'cucumber'
print('r' in text and 'c' in text)
print('z' not in text)

text = 'is there any duck here?'
print('duck' in text)
