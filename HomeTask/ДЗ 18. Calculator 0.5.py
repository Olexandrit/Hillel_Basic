# В цьому завданні важливішою є сама структура класів та код, аніж робота калькулятору
# Всі можливості ті самі що й в усіх калькуляторах до цього,
# **але зробити це за допомогою класів та їх взаємодії між собою**.
#
# Загалом, як має працювати калькулятор:
#
# 1. Привітати користувача
#
# 2. Запропонувати обрати одну з операцій:
#
#   - `+` - складання двох чисел
#
#   - `-` - віднімання двох чисел
#
#   - `*` - множення двох чисел
#
#   - `/` - ділення двох чисел (у разі ділення на 0, результатом має бути нескінченність: ∞)
#
#   - `+++` - складання безлічі чисел
#
# 3. Попросити користувача ввести потрібну кількість чисел
# (у разі операції `+++`, введеня припиняється коли користувач залишає строку пустою)
#
#   - Користувач може ввести бути будь-яке дійсне число
#
#   - У разі, якщо користувач ввів те, що не є дійсним числом,
#   вивести помилку та запитати ввод знову
#
# 4. Виконати операцію
#
# 5. Вивести результат у вигляді `{число} {операція} {число} = {результат}`
# (наприклад: `10.0 - 3.3 = 6.7`).
# У разі операції `+++` вивести всі введені числа з плюсами між ними
# (наприклад: `3.0 + 4.0 + 80.0 + 0.0 + 12.0 = 99.0`)


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


def hello_input():
    print("Вас вітає НеЙмОвІрНиЙ Калькулятор 0.5\n"
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

    return int_operation


class Calculator:
    """
    description
    """

    def __init__(self, number1=0, number2=0):

        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return f'{self.number1} + {self.number2} = {self.number1 + self.number2}'

    def subtraction(self):
        return f'{self.number1} - {self.number2} = {self.number1 - self.number2}'

    def division(self):
        try:
            return f'{self.number1} / {self.number2} = {self.number1 / self.number2}'
        except ZeroDivisionError:
            return "Ділення на 0"

    def multiplication(self):
        return f'{self.number1} * {self.number2} = {self.number1 * self.number2}'

    def speed_sum(self):
        list_numbers = []

        while True:

            string = input("Введіть ціле число(Пробіл - вихід і вивід суми): ")

            if string == " ":
                result = " + ".join([str(i) for i in list_numbers])
                return f'{result} = {sum(list_numbers)}'
            elif string.isdigit():
                list_numbers.append(int(string))
            else:
                print("Це не число!!!")


if __name__ == '__main__':

    int_operation = hello_input()

    calc_object = Calculator()

    if int_operation == 1:
        calc_object.number1, calc_object.number2 = input_numbers()
        result = calc_object.addition()
    elif int_operation == 2:
        calc_object.number1, calc_object.number2 = input_numbers()
        result = calc_object.subtraction()
    elif int_operation == 3:
        calc_object.number1, calc_object.number2 = input_numbers()
        result = calc_object.division()
    elif int_operation == 4:
        calc_object.number1, calc_object.number2 = input_numbers()
        result = calc_object.multiplication()
    elif int_operation == 5:
        result = calc_object.speed_sum()
    else:
        result = "Невідома операція"

    print("Результат: ", result)
