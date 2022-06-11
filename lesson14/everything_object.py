import time


def timer(func):
    def wrap():
        start = time.time()
        result = func()
        print(f'{func.__name__} took {time.time() - start}')

        return result

    return wrap


@timer
def heavy_func():
    sum_ = 0
    for i in range(10000):
        sum_ += i ** i
        
    return sum_


print(f'{str(heavy_func())[:25]}...')


def sleeper(time_):
    def wrapper(func):
        def sleep():
            time.sleep(time_)
            return func()

        return sleep

    return wrapper


@sleeper(3)
def sleepy_func():
    print('I slept well!')


sleepy_func()


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


OPERATIONS = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul,
}

oper = input('Операція: ')
a = int(input('Перше число: '))
b = int(input('Друге число: '))

print()
print(OPERATIONS[oper](a, b))


add.cucumber = True  # так краще не робити
print(add.cucumber)

