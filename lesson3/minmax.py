a = 2
b = 5

print(min(a, b))  # найменше значення
print(max(a, b))  # найбільше значення

c = 10
print(max(a, b, c))  # можна використовувати безліч параметрів

val = 20
val = max(0, min(val, 10))  # обмеження значення між 0 та 10
print(val)

help(min)  # відобразити справку