assert 1 == 1
# assert 1 == 2
# assert 1 == 2, '1 is not 2'


def input_positive_num():
    num = input('Введіть додатне ціле число, пліз: ')
    
    assert num.lstrip('-').isdecimal(), 'Це не число, ну блін :с'
    assert int(num) > 0, 'Це відʼємне число, ну блін :с'
    assert int(num) < 50, 'Ой, це забагато, можна щось менше 50?'
    
    
    return int(num)
    

try:
    num = input_positive_num()
    print('Дякую! ' * num)
except AssertionError as error:
    print(error)


# # Без використання assert
# inp = input('Введіть додатне ціле число, пліз: ')
#
# num = None
# try:
#     num = int(inp)
# except ValueError:
#     print('Це не число, ну блін :с')
#
# if num:
#     if num > 0:
#         print('Дякую! ' * num)
#     else:
#         print('Це відʼємне число, ну блін :с')

