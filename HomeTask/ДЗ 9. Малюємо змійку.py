# Намалювати змійку в терміналі
#
# Відобразити привітання та попередити що зараз буде змійка
# З невиликою затримкою (~0.1 секунди) вивести строку з символом "*" на випадковій відстані від початку строки.
# Випадковим чином змістити "*" на один символ вліво чи вправо, або залишити на місці
# Повторювати пункти 2 та 3 доки користувач не зупине програму натисканням комбінації Ctrl+C
# При закінчинні програми, замість тексту за замовчуванням, вивести обличчя змійки "0_0"
#
#
# P.s. тіло змійки ("*") та обличчя ("0_0") можна змінити за бажанням :)

import time
import random


def print_snake(step_snake):
    print(" " * step_snake + "*")


def print_head_snake(step_snake):
    print(" " * (step_snake - 1) + "0_0")


def run_snake():

    print("Малюємо \U0001F40D. Ctrl-C - stop")

    start_snake = random.randint(10, 15)

    print_snake(start_snake)

    next_step = start_snake

    while True:

        step = random.randint(-1, 1)

        next_step = next_step + step

        try:
            time.sleep(0.1)
            print_snake(next_step)
        except KeyboardInterrupt:
            print_head_snake(next_step)
            exit()


run_snake()
