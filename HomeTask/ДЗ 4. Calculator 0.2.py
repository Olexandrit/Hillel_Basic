
def calculator():

    print("Вас вітає НеЙмОвІрНиЙ Калькулятор 0.2\n Я вмію працювати з операціями над цілими числами: '+ - * /'")

    int_number1 = int(input("Введіть перше ціле число: "))

    int_operation = int(input(
        "Виберіть операцію(число):\n 1 - '+' \n 2 - '-' \n 3 - '/' \n 4 - '*' \n Операція:"
    ))

    int_number2 = int(input("Введіть друге ціле число: "))

    if int_operation == 1:
        result = addition(int_number1, int_number2)
    elif int_operation == 2:
        result = subtraction(int_number1, int_number2)
    elif int_operation == 3:
        result = division(int_number1, int_number2)
    elif int_operation == 4:
        result = multiplication(int_number1, int_number2)
    else:
        result = "Невідома операція"

    print("Результат: ", result)


def addition(number1,  number2):
    return '{0} + {1} = {2}'.format(number1, number2, number1 + number2)


def subtraction(number1,  number2):
    return '{0} - {1} = {2}'.format(number1, number2, number1 - number2)


def division(number1,  number2):
    return '{0} / {1} = {2}'.format(number1, number2, number1 / number2)


def multiplication(number1,  number2):
    return '{0} * {1} = {2}'.format(number1, number2, number1 * number2)


calculator()
