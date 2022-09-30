#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# fiver = list(map(int, input('Введите 5 чисел через пробел: ').split()))
# max=fiver[0]
# for i in range(len(fiver)):
# if fiver[i]>max:
# max=fiver[i]
# print(max)

numbers = int(input(' input amount of numbers: '))
count = 1
arr = []
while( count <= numbers):
    num = int(input(f"input {count} number: "))
    arr.append(num)
    count += 1
print (arr)
max_num = arr[0]
for i in arr:
    if i > max_num:
        max_num = i

print(f' max number is: {max_num}')