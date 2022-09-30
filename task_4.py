# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
n = int(input('Введите число: '))
# startNumber = -n
# while (startNumber <= n):
#     print(startNumber, end=" ")
#     startNumber+=1
for i in range(-n,n+1):
    print(i, end=" ")

# print('введите число')

# value = int(input())

# print (list (range(-value, value+1))