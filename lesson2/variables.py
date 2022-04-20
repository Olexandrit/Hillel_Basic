# Створюємо змінні
hanry = 'White duck'
quacker = 'Black duck'
print('Hanry is', hanry)
print('Quacker is', quacker)

# Змінюємо змінні місцями неправильно
hanry = quacker
quacker = hanry
print('Hanry is', hanry)
print('Quacker is', quacker)

# Змінюємо змінні місцями правильно, але нудно
box = hanry
hanry = quacker
quacker = box
print('Hanry is', hanry)
print('Quacker is', quacker)

# Змінюємо змінні місцями по пайтоновськи
hanry, quacker = quacker, hanry  # 😮
print('Hanry is', hanry)
print('Quacker is', quacker)

# Так НЕ можна називати змінні:
# 🥒 = 'Огурчик'
# 1_variable = 1

# А так можна:
cucumber = '🥒'
variable_1 = 1

print(cucumber)
print(variable_1)
