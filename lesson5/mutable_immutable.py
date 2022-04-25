numbers = [1, 2, 3]  # mutable
numbers_copy = numbers

print(numbers is numbers_copy)
print(numbers)
print(numbers_copy)

numbers.append(4)

print(numbers is numbers_copy)
print(numbers)
print(numbers_copy)

numbers = (1, 2, 3)  # immutable
numbers_copy = numbers_tuple
numbers += (4, 5)
print(numbers is numbers_copy)
print(numbers)
print(numbers_copy)