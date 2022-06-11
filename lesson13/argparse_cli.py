import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
    'integers',  # імʼя аргументу
    type=int,  # очікуваний тип
    nargs='+',  # кількість аргументів
    help='integers to find max value',  # текст підказки для користувача
)

args = parser.parse_args()
print(max(args.integers))


parser.add_argument(
    '--sum',
    dest='action',  # імʼя параметру в парсері
    action='store_const',  # дія яка виконується якщо вказано аргумент, 'store_const' - записати константу
    const=sum,  # константа, яка буде записана в параметр
    default=max,  # значення параметру за замовчуванням
    help='sum the integers (default: find the max)',
)

args = parser.parse_args()
print(args.action(args.integers))


# python3 argparse_cli.py --help
# python3 argparse_cli.py --h
# python3 argparse_cli.py 1 3 7 2 9 5
# python3 argparse_cli.py 1 3 7 2 9 5 --sum
