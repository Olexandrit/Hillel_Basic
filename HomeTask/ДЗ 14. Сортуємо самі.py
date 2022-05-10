
# Не можна використовувати функцію sorted або метод sort
#
# 1. Реалізувати функцію, що приймає список чисел та повертає відсортований список.
#
# 2. Згенерувати список випадкових чисел (використовуйте модуль random) будь-якої довжини. Вивести згенерований список.
#
# 3. Відсортувати згенерований список створеною функцією та вивести відсортований список.

import my_import_list as mil

start = 1

stop = 100

count_number = 15

list_not_sort = mil.generate_list(start, stop, count_number)

print(list_not_sort)

list_sort = mil.my_sorted_list(list_not_sort)

print(list_sort)
