print('2 + 2 =', 2 + 2)
print('10 - 3 =', 10 - 3)

print('10 * 10 =', 10 * 10)
print('20 / 2 =', 20 / 2)
print('5 / 2 =', 5 / 2)

print('5 // 2 =', 5 // 2)  # діленя з результатом типу int
print(type(5 // 2), int(5 / 2))  # int(5 / 2) - еквівалентний результат

print('2 + 2 * 2 =', 2 + 2 * 2)
print('(2 + 2) * 2 =', (2 + 2) * 2)

print('5 % 2 =', 5 % 2)  # modulo, 2 + 2 + (1) = 5
print('11 % 4 =', 11 % 4)  # 4 + 4 + (3) = 11
print(10 % 2)
print(9 % 2)

# А що якщо зі строками? 😳
print('Hello' + 'Cucumber')
print('Hello' + 3)  # не вийде
print('Hello' / 'o')  # не вийде
print(')' * 100)
print('lol' + ')' * 100)

# A також з булевими
print(True + True)
print(False + True)
print(True + True + True + True)

# Робимо відʼємні числа
num = 33
print(-num)
