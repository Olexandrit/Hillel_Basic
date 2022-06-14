import time


def dummy(func):
    print(func)
    return func


@dummy
def hi():
    print('Hi!')


hi()


def timer(func):
    def wrap():
        start = time.time()
        result = func()
        end = time.time()

        print(f'Function took {end - start}s')

        return result
    return wrap


def stringify(func):
    return lambda: str(func())


@stringify
@timer
def heavy_func():
    sum_ = 0
    for i in range(10000):
        sum_ += i ** i

    return sum_


print(type(heavy_func()))


def classname(cls):
    cls.classname = cls.__name__

    return cls


@classname
class Dog:
    def __init__(self, name):
        self.name = name


d = Dog('Bobby')
print(d.name)
print(d.classname)
