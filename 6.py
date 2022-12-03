# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def summa_add_index(list):
#     summa = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             summa += list[i]
#     print(f"Сумма равна: {summa}")


# list = list(map(int, input("Введите числа через пробел:\n").split()))
# summa_add_index(list)

# ----------------------------------------------------

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй
#  и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# def multi_list(list):
#     l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
#     new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
#     print(new_list)


# list = list(map(int, input("Введите числа через пробел:\n").split()))
# print(list)
# multi_list(list)

# ----------------------------------------------------------------

# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i%1,2) for i in list if i%1 != 10]
# print(max(new_list) - min(new_list))

# ------------------------------------------------------------

# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# ostatok = []
# digit = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while digit > 0:
#     ostatok.append(str(digit%2))
#     digit //=2
# print(*ostatok[::-1], sep="")

# ostatok = ""
# digit = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while digit > 0:
#     ostatok = str(digit%2) + ostatok
#     digit //=2
# print(ostatok)

# ---------------------------------------------------


# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть 
# так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def to_directions_fibonacci(num):
#     fib = {-2: -1, -1: 1, 0: 0, 1: 1}
#     i = 2
#     while i <= num:
#         fib.update({i: fib[i-2] + fib[i-1]})
#         fib.update({-i: fib[-i+2] - fib[-i+1]})
#         i += 1
#     return fib

# print(to_directions_fibonacci(8))


# mem = {1: 1, 2: 1}
 
 
# def fib(n):
#     if n not in mem:
#         mem[n] = fib(n - 2) - fib(n + 1)
 
#     return mem[n]
 
 
# print(fib(8))
# print(mem)




def fib(n):
    if n>=0:
       id_x = range(n+1)
       x = [0,1]
       for k in id_x[2:]:
           x.append(x[k-1] + x[k-2]) 
       return x[n]
    else:
       n=-(n-1)
       id_x = range(n+1)
       x = [1,0]
       for k in id_x[2:]:
           x.append(x[k-2] - x[k-1]) 
       x.reverse()
    return x[0]



n = int(input("Введите число: "))
for i in range(-n, n):
   print(fib(i), end = " ")