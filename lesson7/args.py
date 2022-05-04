def avg(*nums):
    print(nums)
    return sum(nums) / len(nums)


print(avg(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))


def list_name(name, surname):
    print(f'Name: {name}')
    print(f'Surname: {surname}')


person = 'Boris Jhonsonuk'
print(person.split(' '))

list_name(*person.split(' '))


def text_multiplier(**kwargs):
    print(type(kwargs), kwargs)

    for key, value in kwargs.items():
        print(key * value)


text_multiplier(cucumber=100, hello=10, i=3)


def list_ducks(hanry, quacker, rose):
    print(f'Hanry is {hanry} duck')
    print(f'Quacker is {quacker} duck')
    print(f'Rose is {rose} duck')


ducks = {
    'quacker': 'black',
    'hanry': 'white',
    'rose': 'brown',
}

list_ducks(**ducks)