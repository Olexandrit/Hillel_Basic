# У параллельному всесвіті існує деякий сейф, в ньому мафія зберігає компромат на Гері.
# Це "розумний мультивсесвітний" сейф - на ньому є сервер який дозволяє відкрити його,
# але доступ до цього серверу є тільки з нашого всесвіту.
# Тому Гері не може сам підібрати код та відкрити сейф. Вам треба допомогти Гері зламати його.
#
# Код до сейфу складається з 3 цифр (наприклад 123 або 039).
# Кожні 60 секунд сейф змінює код на новий, випадковий.
# Тож у вас є лише 60 секунд щоб вгадати код.
# Серверу сейфу потрібна приблизно секунда щоб перевірити чи код підходить.
#
# АПІ для відкриття сейфу доступно за посиланням: http://code.qqmber.wtf/guess/
#
# Метод запиту - POST, формат тіла запиту - JSON.
#
# У JSON має бути лише одне поле password і значення для перевірки.
#
# Наприклад:
#
# {"password": "042"}
#
# У відповідь сервер пришле код статусу 200 якщо пароль підійшов, або 400 якщо ні.
#
# Додатково, документацію API можна знайти тут: http://code.qqmber.wtf/docs/
#
# Тож, треба створити скрипт який перебере всі можливі паролі (від 000 до 999)
# менш ніж за хвилину і знайде потрібний.
#
# Врятуйте Гері 💪
#
# Приклад результату: https://asciinema.org/a/U8bJkcHvCjNVV7duVFyqYJSO1
#
# P.s. Використовуйте threading, multiprocessing або asyncio

import threading
import requests


def create_list_numbers(threads, max_number):

    full_list = [i for i in range(0, max_number)]

    list_f = full_list

    portion = round(max_number / threads)

    step = 0

    result = []

    while step != threads:

        step = step + 1

        list_a = list_f[0:portion]

        if step == threads:
            list_a = list_f
        else:
            list_f = list_f[portion:]

        result.append(list_a)

    return result


def post_code_qqmber_wtf(str_number):
    url = 'http://code.qqmber.wtf/guess/'
    data = {'password': f'{str_number}'}

    response = requests.post(url, json=data)
    print(f'Check: {str_number}, {response}')

    status_code = response.status_code

    if status_code == 200:
        print(f'Done, password in {str_number}')

    return status_code


def run_generate_password(list_numbers):

    for i in list_numbers:

        str_number = str(i).rjust(3, "0")

        result = post_code_qqmber_wtf(str_number)


if __name__ == '__main__':

    THREADS = 100

    MAX_NUMBER = 1000

    list_thread = create_list_numbers(THREADS, MAX_NUMBER)

    for list_numbers in list_thread:

        thread = threading.Thread(target=run_generate_password, args=(list_numbers, ))
        thread.start()
