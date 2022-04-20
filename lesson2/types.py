number = 10  # Integer (int) - ціле число
text = 'Cucumber'  # String (str) - строка (символов)
decimal = 2.5  # Float (float) - число с (плавающей) запятой
truth = True  # Boolean (bool) - логічне значення (Булеве)
lie = False

# Дивимось який тип данних має змінна
print(type(number))
print(type(text))
print(type(decimal))
print(type(truth))

# Приведення типів
print(str(number), type(str(number)))


print(int(text))  # Не вийде, отримаємо помилку
print(int('5'))  # 👍

print(int(decimal))  # Результат: 2
print(int(2.9))  # Результат: 2
print(round(2.9))  # Результат: 3 (округлення)

print(int(truth), int(lie))
print(bool(number))  # Результат: True
print(bool(text))  # Результат: True
print(bool(0))  # Результат: False
print(bool(''))  # Результат: False
