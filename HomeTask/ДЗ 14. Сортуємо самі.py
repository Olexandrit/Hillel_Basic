
# Не можна використовувати функцію sorted або метод sort
#
# 1. Реалізувати функцію, що приймає список чисел та повертає відсортований список.
#
# 2. Згенерувати список випадкових чисел (використовуйте модуль random) будь-якої довжини. Вивести згенерований список.
#
# 3. Відсортувати згенерований список створеною функцією та вивести відсортований список.


import my_import_list as mil

START = 1

STOP = 100

COUNT_NUMBER = 15

list_not_sort = mil.generate_list(START, STOP, COUNT_NUMBER)

print(list_not_sort)

list_sort = mil.my_sorted_list(list_not_sort)

print(list_sort)
