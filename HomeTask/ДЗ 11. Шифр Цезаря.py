# Шифр Цезаря - один із найдавніших відомих шифрів. Схема шифрування дуже проста - використовується зсув літери алфавіту на фіксоване число позицій. Алфавіт "зациклюється", тобто букви в кінці алфавіту перетворюються на букви початку алфавіту.
#
# Наприклад, слово "Cucumber" зашифроване цим способом з зсувом 3 (три) стане "Fxfxpehu", а "Zebra" стане "Cheud".
#
# Завдання, зробити шифрувальник та дешифрувальник для шифру Цезаря. Алфавіт - англійський.
#
# Запитати в користувача:
# Чи він хоче зашифрувати або розшифрувати текст.
# Текст для шифрування/дешифрування.
# Ключ зсуву.
# Зашифрувати або розшифрувати текст. Змінювати тільки літери a-z, A-Z, усі інші символи залишати як є.
# Вивести результат.
#
# P.s. Рекомендується використовувати ord та chr.

# encryption
def encryption(string, key):

    list_letter = list(string)

    new_list_letter = list()

    min_upper_code = 65
    max_upper_code = 90

    min_lowcase_code = 97
    max_lowcase_code = 122

    for w in list_letter:

        code = ord(w)

        # Визначаємо чи код букви належить вверхньому/нижньому регістру

        # upper
        if min_upper_code <= code <= max_upper_code:

            new_code = min_upper_code + (code - min_upper_code + key) % (max_upper_code - min_upper_code + 1)

        #  lowcase
        elif min_lowcase_code <= code <= max_lowcase_code:

            new_code = min_lowcase_code + (code - min_lowcase_code + key) % (max_lowcase_code - min_lowcase_code + 1)

        else:

            new_code = code

        new_letter = chr(new_code)

        new_list_letter.append(new_letter)

    return new_list_letter


def decryption(string, key):

    list_letter = list(string)

    new_list_letter = list()

    min_upper_code = 65
    max_upper_code = 90

    min_lowcase_code = 97
    max_lowcase_code = 122

    for w in list_letter:

        code = ord(w)

        # Визначаємо чи код букви належить вверхньому/нижньому регістру

        # upper
        if min_upper_code <= code <= max_upper_code:

            new_code = min_upper_code + (code - min_upper_code - key) % (max_upper_code - min_upper_code + 1)

        #  lowcase
        elif min_lowcase_code <= code <= max_lowcase_code:

            new_code = min_lowcase_code + (code - min_lowcase_code - key) % (max_lowcase_code - min_lowcase_code + 1)

        else:

            new_code = code

        new_letter = chr(new_code)

        new_list_letter.append(new_letter)

    return new_list_letter


def cesarean_code():

    key = 3

    new_list_letter = list()

    oper_encrypt = 1

    oper_decrypt = 2

    print("Це шифр Цезаря")

    value = int(input("Потрібно 1-зашифрувати чи 2-розшифрувати рядок?\nВиберіть дію: "))

    if value in (oper_encrypt, oper_decrypt):

        string = input("Введіть рядок англійською мовою: ")

        print(f'Введений рядок {string}')

        if value == oper_encrypt:
            new_list_letter = encryption(string, key)
        elif value == oper_decrypt:
            new_list_letter = decryption(string, key)

    else:
        print("Невідома дія!!! Повторіть програму")
        exit()

    new_string = "".join(new_list_letter)

    print(f'Результат: {new_string}')


cesarean_code()

