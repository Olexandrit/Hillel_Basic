
print("Привіт. Давай порівняємо два цілих числа: ")

int_num1 = int(input("Введи перше число: "))

int_num2 = int(input("Введи друге число: "))

if int_num1 > int_num2:
    print("Перше число більше за друге")
elif int_num2 > int_num1:
    print("Друге число більше за перше")
else:
    print("Числа рівні")
