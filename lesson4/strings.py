string = 'Cucumber'
print(string.lower())
print(string.upper())
string = 'cUcUmBeR'
print(string.capitalize())
print(string.swapcase())

string = '    '
print(bool(string))  # True
print(string.isspace())
string = 'abcdefcucumber'
print(string.isalpha())
print(string.isdecimal())
string = '350'
print(string.isalpha())
print(string.isdecimal())

string = 'Cucumber or not?!'
print(string.startswith('Cucumber'))
print(string.endswith('?!'))

string = 'cucumber cucumber cucumber banana cucumber'
print(string.count('cucumber'))
print(string.replace('banana', 'cucumber'))
print(string.replace('banana', 'cucumber').count('cucumber'))

string = 'cucumber'
#         01234567
#        -87654321
print(string[0])
print(string[3])
print(string[8])  # помилка
print(string[-1])
print(string[-3])

print(string[4])
print(string.index('m'))
print(string[string.index('m')])
print(string.index('u'))
print(string.index('um'))
string.index('a')  # помилка
print(string.find('a'))

# Форматування
template = 'I like {}'
liked = 'cucumbers'
other_liked = 'bananas'
print(template.format(liked))
print(template.format(other_liked))

template = 'I like {} and {}'
print(template.format(liked, other_liked))

template = 'I like {1} and {0}'
print(template.format(liked, other_liked))

template = 'I like {obj} - so I will buy some {obj}'
print(template.format(obj=liked))

template = 'I like {0} - so I will buy some {0}'
print(template.format(liked))

# Трошки магії 🪄
print(f'I like {liked * 10}')

# Slicing (зріз)
text = 'Don\'t like cucumbers'  # \ - екранування
#       012 3456789...
print(text[6])  # елемент з індексом 6
print(text[6:])  # всі елементи від індексу 6 до кінця
print(text[6:10])  # всі елементи від індексу 6 до індексу 10 (не включаючи)
# кожен другий елементи від індексу 6 до індексу 10 (не включаючи)
print(text[6:10:2])

nums = '0123456789'
#       0123456789
print(nums[::2])  # кожен другий елемент
