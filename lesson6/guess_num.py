import random

print('Дурна гра вгадай число 🎰 (від 0 до 100)')
secret_num = random.randint(0, 100)
guess = None

while guess != secret_num:
    guess = int(input('Hy, вгадуй: '))

    if guess < secret_num:
        print('Ні, твоє число менше за загадане')
    if guess > secret_num:
        print('Не, твоё число більше за загадане')

print('Ты вгадав!!! Але призів не буде 🙃')