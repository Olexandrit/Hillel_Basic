def i_have_cucumber():
    cucumber = '🥒'
    print(cucumber)


print(cucumber)  # Помилка

# ---

outer_var = 'I\'m outside'


def test_var():
    inner_var = 'I\'m inside'
    print(outer_var)
    print(inner_var)


test_var()

print(outer_var)
print(inner_var)  # Помилка

# ---

name = 'Taras'


def say_hi():
    name = 'Vasyl'
    print(f'Hi, {name}')


def say_bye():
    print(f'Goodbye, {name}')


say_hi()
say_bye()