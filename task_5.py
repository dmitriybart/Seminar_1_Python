#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
import math


number = float (input('Введите дробное число: '))
num_result = number*10
if number - int(number) == 0:
    print('нет')
else:
    print (math.floor(num_result)%10)

# f = float(input())
# d = int( (f*10) % 10 )
# print(f, d, sep=" -> ")