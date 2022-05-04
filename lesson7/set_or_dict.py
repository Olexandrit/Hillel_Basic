# Тут все добре
letters_set = {'a', 'b', 'c'}  # в set лише значення
letters_dict = {'a': 1, 'b': 2, 'c': 3}  # в dict ключ та значення
print(type(letters_set))
print(type(letters_dict))

# Але якщо вони пусті...
empty_set = {}
empty_dict = {}
# виглядають однаково
print(type(empty_set), type(empty_dict))  # і обидва dict

empty_set = set()  # пустий set треба робити так
empty_dict = dict()
print(type(empty_set), type(empty_dict))  # тепер файно