# A comment.
# Не забудьте створити віртуальне середовище (virtual environment) та файл requirements.txt.
# Директорії з віртуальним середовищем на GitHub бути НЕ має
# (для цього зручно використати файл .gitignore).
# Можна створити окремий репозиторій.
#
# Як відомо, кицьок багато не буває.
# Ця програма має скачувати вказану кількість зображень з кицьками.
# Кицьок брати з цього сервісу: http://placekitten.com
#
# Програма має приймати наступні аргументи (використовуйте argparse):
# amount - ціле число, кількість файлів з кицьками що буде створено.
# out_dir - назва директорії у яку буде збережено кицьок.
# За замовчуванням, директорія у якій користувач знаходиться.
# --gray - якщо вказано, створити чорно-білих кицьок.
# Створити директорію вказану в аргументі out_dir, якщо ії не існує.
# Обрати випадкову ширину та висоту зображення (від 100 до 1000 пікселів).

# Відіслати запит на http://placekitten.com/{ширина}/{висота}
# (якщо вказано аргумент --gray додати /g/ перед розмірами).
# Наприклад http://placekitten.com/300/500 або http://placekitten.com/g/300/500.
# Записати тіло (у якому зображення) відповіді на запит,
# у файл (який має знаходитись у вказаній в out_dir директорії).
# Назва файлу - будь яка, але унікальна серед інших файлів створених програмою. Формат - jpeg.
# Повторити пункти 3 - 5 стільки разів скільки користувач вкаже в аргументі amount.


import argparse
import random
import requests
import os

DEFAULT_FOLDER = "fluffy_cats"

def run_argparse():
    """
    description
    :return:
    """
    parser = argparse.ArgumentParser(description='Process download cats')
    parser.add_argument(
        'amount',  # імʼя аргументу
        type=int,  # очікуваний тип
        # nargs=1,  # кількість аргументів
        help='count cats downloads',  # текст підказки для користувача
    )

    parser.add_argument(
        '--out_dir',  # імʼя аргументу
        dest='out_dir',
        type=str,  # очікуваний тип
        # nargs=1,  # кількість аргументів
        default=DEFAULT_FOLDER,  # значення параметру за замовчуванням
        help=f'download folder (default: {DEFAULT_FOLDER})',  # текст підказки для користувача
    )

    parser.add_argument(
        '--gray',
        dest='gray',  # імʼя параметру в парсері
        action="store_true",  # дія яка виконується якщо вказано аргумент, 'store_const' - записати константу
        help='якщо вказано, створити чорно-білих кицьок. ',
    )

    args = parser.parse_args()

    return args


def create_folder_download(directory_name):
    """
    description
    :param directory_name:
    :return:
    """
    # create folder
    # path
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory_name)
    print(path)

    # find folder
    if not os.path.exists(path):
        # Create the directory
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
            return ""

    return path


def downloads_fluffy_cats(amount, catalog_cats, use_gray=""):
    """
    description
    :param amount:
    :param catalog_cats:
    :param use_gray:
    :return:
    """
    for i in range(0, amount):

        width = random.randint(100, 1000)
        height = random.randint(100, 1000)

        text_request = f'http://placekitten.com/{use_gray}/{width}/{height}'

        response = requests.get(text_request)
        if response:

            print(f'Скачую котика розміром {width}x{height}')

            name_file = f'cat_{i}_{width}_{height}.jpeg'
            path_file = os.path.join(catalog_cats, name_file)

            with open(path_file, "wb") as file:
                file.write(response.content)
                file.close()

        else:
            print('Якась проблема. Не вдалося скачати котика')
            print(response.status_code)
            print(response.text)


if __name__ == '__main__':

    args = run_argparse()

    amount = args.amount

    directory_name = args.out_dir

    use_gray = args.gray

    if use_gray:
        GRAY = "g"
        print(f'Будемо скачувати {amount} сірих котиків в каталог {directory_name}')
    else:
        GRAY = ""
        print(f'Будемо скачувати {amount} кольорових котиків в каталог {directory_name}')

    catalog_cats = create_folder_download(directory_name)

    downloads_fluffy_cats(amount, catalog_cats, GRAY)
