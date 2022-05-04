# f(x, y) = x^2 + y^2
def f(x, y):  # def - define (визначити); (x, y) - аргументи функції
    return x**2 + y**2  # return - повернути/віддати


# дві пусті строки навколо функції
x = 2
y = 3

z = f(x, y)
print(z)

z = f(5, 8)
print(z)

print(f(4, 3))

print(f(x=2, y=3))


def say_hi():
    print('Hi!')


say_hi()

z = say_hi()
print(z)  # None