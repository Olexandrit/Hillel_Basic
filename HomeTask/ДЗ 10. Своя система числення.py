# Конвертер з деякої системи числення до десяткової
#
# Обрати собі систему числення з базою більше 10, але не 16. (наприклад 11, 23, ...).
# Запросити користувача ввести деяке число використовуючи обрану систему числення.
# Конвертувати введене число з обраної системи числення у десяткову.
# Вивести результат.


def base36():
    base = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35

    }

    return base


def intro():
    print(f'Ласкаво просимо у конвертер системи числення з базою 36 в десяткову\n'
          f'Допустимі символи та їх значення:')

    print(base36())


def convert36_to_10(string):
    number_systems = 36

    base = base36()

    string_upper = string.upper()

    list_string = list(string_upper)

    len_index = len(list_string)

    num_step = len_index - 1
    index_list = 0

    list_numbers = []
    while len_index != index_list:

        val_list = list_string[index_list]

        val_base = base.get(val_list)

        if val_base is None:
            return "Вхідні дані не коректні для системі з базою 36. Див. опис бази"
        else:
            number = val_base * (number_systems ** num_step)
            list_numbers.append(number)

        num_step = num_step - 1
        index_list = index_list + 1

    return sum(list_numbers)


def calculator36_to_10():

    intro()

    string = input("Введіть число в базі 36: ")

    result = convert36_to_10(string)

    print(f'Ваше число в десятковій системі числення: {result}')


calculator36_to_10()
