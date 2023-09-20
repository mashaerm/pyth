# Python, JS
# C#/C/C++, Java
# n = 5 # -> class <'int'> -> []
# int n = 5; -> []
# print(type(n))

# name = input("Введите свое имя: ")
# print(f'Привет, {name}!') # $"{}" char n = '5';
# print(type(name))
# int(), str(), float()

# n = '234'
# print(int(n) - 10) # int() делает перевод из str в int

# n = 2.871
# print(int(n))

# n = int(input("Введите число: "))
# print(f'{n} * 2 = {n * 2}')

# n = float(input("Введите дробное число: "))
# print(f'{n} * 2 = {n * 2}')


# n = int(input("Введите целое число: "))
# print(f'{n} + 5 = {n + 5}')
# print(f'{n} - 7 = {n - 7}')
# print(f'{n} * 3 = {n * 3}')
# # 7 : 3 = 2(ост. 1)
# print(f'{n} : 3 = {n // 3} (ост. {n % 3})')
# # 7 : 3 = 2.3333
# print(f'{n} : 3 = {n / 3}')
# print(f'{n}^0.5 = {n ** 0.5}')



# s
# print(int(n > 8))
# bool(Boolean) - True(1) or False(0)
# and(&&) - конъюнкция(логическое умножение)
# or(||) - дизъюнкция(логическое сложение)
# not - отрицание
# in ???

# print(n % 2 == 0 and n > 10 or n % 12 == 0)


# Task 1

# n = int(input("Введите кол-во километров, которое Вы проезжаете за день: "))
# m = int(input("Введите общий киллометраж: "))
# print((m + n - 1) // n)


# Отрицательное деление
# -7 // 2 = (-4) * 2 + 1
# -12 // 5 = (-3) * 5 + 3 
# print(-12 % 5)


# Task 3

# a = int(input('Введите количество учеников в первом классе:'))
# b = int(input('Введите количество учеников во втором классе:'))
# c = int(input('Введите количество учеников в третьем классе:'))
# sum1 = a//2 + a % 2
# sum2 = b//2 + b % 2
# sum3 = c//2 + c % 2
# print(sum1 + sum2 + sum3)


# Task 5
#i = int(input("В какой вагон сел Витя: "))
#j = int(input("Какой вагон указан на табличке: "))
#if i == j:
#    print("Нужна дополнительная информация")
#else:
    #print(i + j - 1)


# Task 7
#year = int(input())
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#  print('YES')
#else:
#    print('NO')

# name = "Ivan"
# #       0123
# print(name[0])
# foreach - C#
# for element in "Hello", 123, 34.125, True, 'a':
#     print(element * 2)
# 0: element = "Hello"
# 1: element = 123
# 2: element = 34.125
# ...
# range и for между собой НИКАК НЕ СВЯЗАНЫ!!!
# range(begin=необязательный(0), end=обязательный, step=необязательный(+1))
# print(*range(5))
# # 0 1 2 3 4
# print(*range(5, 0, -1))
# print(*range(5, 13, 2))
# print(*range(2, 10))
# print(*range(0, 8, 2))

# for i in range(5):
#     # print(i, end=' ')
#     print(i, end='!\n')

# print(1, end=', ')
# print(2, end='. ')
# print(3, end='!\n')
# # print()
# print("Hello")

# print("Ivan")


# from numpy import arange

# for i in arange(0.0, 1.23, 0.01):
#     print(i)


# Task 9
# n = int(input("Input number: "))
# result = 1
# while n > 1:
#     result *= n # result = result * n
#     n -= 1
# print(result)
# Task 11

# n = int(input("Введите число: "))
# first_fib = 0
# second_fib = 1
# i = 2 # Первые два числа уже известны
# while second_fib < n:
#     next_fib = first_fib + second_fib
#     # 0 1 1 2 3 5 8
#     # 1 + 1 = 2
#     first_fib = second_fib
#     second_fib = next_fib
#     i += 1
#     if second_fib > n:
#         i = -1
# print(i)


# Task 15
# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# max_massa = min_massa = x
# for i in range(n - 1): 
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x: 
#         min_massa = x
# print(min_massa, max_massa)


# Task 13
# n = int(input("Введите кол-во дней: "))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input("Введите температуру: "))
#     if temp > 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)

# Task 10

# n = int(input('Введите число монеток: '))
# from random import randint
# minmonFr = minmonSec = 0
# for i in range(n):
#     number = randint(0, 1)
#     print(number, end=' ')
#     if number > 0: minmonFr += 1
#     else: minmonSec += 1
# if minmonFr > minmonSec:
#     print(f'Нужно перевернуть монеток: {minmonSec}')
# else:
#     print(f'Нужно перевернуть монеток: {minmonFr}')

# Task 12

# S = int(input('Введите сумму чисел: '))
# P = int(input('Введите произведение чисел: '))
# number = 0
# for x in range(S):
#     for y in range(S):
#         if x + y == S and x * y == P and x <= 1000 and y <= 1000:
#             number += 1
#             print(f'Загаданные числа: {x, y}')

# Task 14

n = int(input('Введите число N: '))
temp = 0
result = 1
while result < n + 1:
    print(result)
    temp += 1
    result = 2 ** temp