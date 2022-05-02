# Порахувати кількість зустрічей кожного символу у тексті
#
# 1. Вивести привітання
#
# 2. Запросити користувача ввести текст
#
# 3. Порахувати кількість зустрічей для кожного символу у тексті
#
# 4. Вивести результат для кожного символа який був зустрінутий

from collections import Counter

def count_symbol_in_string(string):

    string = string.lower()

    string = string.replace(" ", "")

    counter = Counter(string)

    dict_symbol = dict(counter)

    return dict_symbol


def symbols_in_string():

    print("Привіт, я вмію рахувати кількість символів в рядку!:)")

    string = input("Введіть рядок символів: ")

    dict_symbol = count_symbol_in_string(string)

    for key in dict_symbol:
        print(f'Символ "{key}" зустрічається {dict_symbol.get(key)} разів')


symbols_in_string()
