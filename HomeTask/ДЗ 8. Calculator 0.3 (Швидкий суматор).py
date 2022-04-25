# Покращити ЧУДОВИЙ калькулятор.
#
# Додати операцію "+++" - операція складання багатьох чисел.
# Для цієї операції треба запитувати у користувача ввести число безліч разів.
# Доти, доки користувач не введе пусту строку.
# Просумувати всі введені користувачем числа та вивести результат.
# Вивести ♾ (inf) у разі ділення на 0, зробити це за допомогою try ... except.

def calculator():
    print("Вас вітає НеЙмОвІрНиЙ Калькулятор 0.3\n"
          "Я вмію працювати з операціями над цілими числами: '+ - * / \n"
          "Нова функція: +++(Швидкий суматор)'")

    operations_dict = {1: "+", 2: "-", 3: "/", 4: "*", 5: "+++"}

    list_operation_note = []
    for key in operations_dict:
        str = f'{key} -> "{operations_dict[key]}"'
        list_operation_note.append(str)

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

    int_number1 = int(input("Введіть перше ціле число: "))

    int_number2 = int(input("Введіть друге ціле число: "))

    return  int_number1, int_number2


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

        str = input("Введіть ціле число(Пробіл - вихід і вивід суми): ")

        if str == " ":
            return sum(list_numbers)
        elif str.isdigit():
            list_numbers.append(int(str))
        else:
            print("Це не число!!!")

calculator()
