# Покращити ЧУДОВИЙ калькулятор.
#
# Додати операцію "+++" - операція складання багатьох чисел.
# Для цієї операції треба запитувати у користувача ввести число безліч разів.
# Доти, доки користувач не введе пусту строку.
# Просумувати всі введені користувачем числа та вивести результат.
# Вивести ♾ (inf) у разі ділення на 0, зробити це за допомогою try ... except.

def calculator():
    print("Вас вітає НеЙмОвІрНиЙ Калькулятор 0.4\n"
          "Я вмію працювати з операціями над цілими числами: '+ - * / \n"
          "Нова функція: +++(Швидкий суматор)'")

    operations_dict = {1: "+", 2: "-", 3: "/", 4: "*", 5: "+++"}

    list_operation_note = []
    for key in operations_dict:
        string = f'{key} -> "{operations_dict[key]}"'
        list_operation_note.append(string)

    str_operations = '\n'.join(list_operation_note)

    int_operation = int(input(
        "Виберіть операцію(число):\n"
        f'{str_operations}\n'
        "Операція: "
    ))

    print(f'"Операція: {operations_dict[int_operation]}"')

    if int_operation == 1:
        result = addition()
    elif int_operation == 2:
        result = subtraction()
    elif int_operation == 3:
        result = division()
    elif int_operation == 4:
        result = multiplication()
    elif int_operation == 5:
        result = speed_sum()
    else:
        result = "Невідома операція"

    print("Результат: ", result)


def input_numbers():

    number1 = input_number1()

    number2 = input_number2()

    return number1, number2


def input_number1():

    string = "Введіть перше число: "

    number = input_number(string)

    return number


def input_number2():

    string = "Введіть друге число: "

    number = input_number(string)

    return number


def input_number(input_text):

    number = 0

    string = input(input_text)

    try:
        number = float(string)
    except:
        print("Це не число. Введіть число!")
        return input_number(input_text)

    return number


def addition():
    number1, number2 = input_numbers()

    return '{0} + {1} = {2}'.format(number1, number2, number1 + number2)


def subtraction():
    number1, number2 = input_numbers()

    return '{0} - {1} = {2}'.format(number1, number2, number1 - number2)


def division():
    number1, number2 = input_numbers()

    try:
        result = number1 / number2
    except ZeroDivisionError:
        return "Ділення на 0"

    return '{0} / {1} = {2}'.format(number1, number2, result)


def multiplication():
    number1, number2 = input_numbers()

    return '{0} * {1} = {2}'.format(number1, number2, number1 * number2)


def speed_sum():
    list_numbers = []

    while True:

        string = input("Введіть ціле число(Пробіл - вихід і вивід суми): ")

        if string == " ":
            return sum(list_numbers)
        elif string.isdigit():
            list_numbers.append(int(string))
        else:
            print("Це не число!!!")


calculator()
