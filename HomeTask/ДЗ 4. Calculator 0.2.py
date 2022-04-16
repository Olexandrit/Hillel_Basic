
def calculator():

    print("Вас вітає НеЙмОвІрНиЙ Калькулятор 0.2\n Я вмію тільки додавати 2 цілих числа")

    string1 = input("Введіть перше число: ")

    string2 = input("Введіть друге число: ")

    num1 = int(string1)

    num2 = int(string2)

    sum = num1 + num2

    print(num1, "+", num2, "=", sum)


calculator()
