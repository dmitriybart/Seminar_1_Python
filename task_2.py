#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
c
b = int(input('Введите второе число: '))
if a**2 == b:
    print('Да')
elif b**2 == a:
    print('Да')
else: print('Нет')