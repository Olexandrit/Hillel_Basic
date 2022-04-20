alphabet = 'abcdefghijklmnopqrstuvwxyz'

# для кожної букви (letter) в змінній алфавіт (alphabet)
for letter in alphabet:
    print(letter)  # вивести букву (letter)

digits = '1352462819385018234745'
for digit in digits:
    if int(digit) < 5:
        print(digit)

counter = 0
while counter <= 100:  # доки змінна лічильник (counter) менше або дорівнює 100
    print(counter)  # вивести значення змінної лічильник (counter)
    # та збільшити значення змінної лічильник (counter) на 1
    counter = counter + 1

text = None
while text != '3':
    text = input('Введіть "3": ')
print('Дяк :3')

for num in range(10):  # для кожного числа від 0 до 10 (не включаючи 10)
    print(num)

for num in range(10, 20):  # для кожного числа від 10 до 20 (не включаючи 20)
    print(num)

for num in range(10, 20, 2):  # для кожного другого числа від 10 до 20 (не включаючи 20)
    print(num)
