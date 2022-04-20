# Унарні оператори
num = 3
print(num)
num = -num
print(num)
num = +num
print(num)

# Бінарні оператори
num_a = 1
num_b = 2

result = num_a + num_b
print(result)

result = num_a / num_b
print(result)

result = num_a == num_b
print(result)

# Тернарний оператор
num_a = 0
num_b = 42

result = num_a if num_a != 0 else num_b
print(result)

# Трошки магії 🪄
result = num_a or num_b
print(result)

# Коли магія не працює
result = num_a if num_a > 0 else num_b
print(result)

# Трошки прокачаної магії 🧙‍♂️
result = num_a and num_b
print(result)

num_str = ''
result = num_str and int(num_str)  # уникаємо помилки
print(result)
