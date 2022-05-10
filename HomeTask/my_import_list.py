
import random

def get_min_value(list_value):

    return min(list_value)


def del_min_value(list_value, value):

    list_value.remove(value)


def append_val_list(list_value, value):

    list_value.append(value)


def my_sorted_list(list_not_sort):

    len_list = len(list_not_sort)

    list_sort = []

    while len_list != 0:

        min_val = get_min_value(list_not_sort)

        append_val_list(list_sort, min_val)

        del_min_value(list_not_sort, min_val)

        len_list = len(list_not_sort)

    return list_sort


def generate_list(start, stop, count_numbers=15):

    """Generate new list random int
    :param start:(int) number start
    :param stop:(int) number stop
    :param count_numbers: (int) count number
    :return: list generate numbers
    """
    new_list = random.sample(range(start, stop), count_numbers)

    random.shuffle(new_list)

    return new_list
