# Задача №30: Вычислить число c заданной точностью d. Пример:
# при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

# from math import pi
# from decimal import *
# from math import factorial


# N =  int(input("Введите число для заданной точности числа Пи: "))
# print(round(pi, N))

# def chudnovsky(n):
#     pi1 = Decimal(0)
#     k = 0
#     while k < n:
#         pi1 += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
#         k += 1
#     pi1 = pi1 * Decimal(10005).sqrt() / 4270934400
#     pi1 = pi1**(-1)
#     return pi1

# A = N + 1
# getcontext().prec = A # точность (число знаков)
# out = chudnovsky(A)
# print(out)


# def pi_(d=0.001):
#     s = 0
#     b = 1
#     sgn = 1
#     while True:
#         a = 4 / b
#         s = s + sgn * a
#         if a < d:
#             return s
#         sgn =- sgn
#         b = b + 2
 
 
# print(pi_())

# 2 Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]


# num = int(input("Введите число: "))
# i = 2
# list = []
# old = num
# while i <= num:
#     if num % i == 0:
#         list.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old}: {list}")


# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
# -> [2, 4, 5, 9]


# lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
# print(lst)
# for i in lst:
#    if lst.count(i) == 1:
#        print((i), end = " ")



# 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint


# def write_file(st):
#     with open('testfile.txt', 'w') as data:
#         data.write(st)
#         print("Данные записаны в файл testfile.txt")


# max_limit = 100
# k = int(input('Введите натуральную степень k: '))
# koeff = [randint(0, max_limit) for i in range(k)]+[randint(1, max_limit)]
# poly ='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

# poly = poly.replace('x^1+', 'x+')
# poly = poly.replace('x^0', '')
# poly += ('','1')[poly[-1]=='+']
# poly = (poly, poly[:-2])[poly[-2:]=='^1']
# print(poly)

# write_file(poly)


# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными,
#  так и отрицательными. Степени многочленов могут отличаться.

import random

# # запись в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

# # создание случайного числа от 0 до 100
def rnd():
    return random.randint(0,101)

# # создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
# # создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# # получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# # получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# # разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    


# # создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("1.txt", create_str(koef1))
write_file("2.txt", create_str(koef2))

# нахождение суммы многочлена
with open('1.txt', 'r') as data:
    st1 = data.readlines()
with open('2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("3.txt", create_str(lst_new))
with open('3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")