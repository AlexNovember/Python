# 1. Напишите программу, которая принимает на вход число N и выдаёт 
#     последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81


# 2. Для натурального n создать список, 
#    состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 4: [1, 4, 7, 10, 13] 

# 3. Напишите программу, в которой пользователь будет задавать две строки, 
#    а программа - определять количество вхождений одной строки в другой.

# s1 = 'aa ab aba ewfwef'
# s2 = 'aba'

# print(s1.count(s2))


# print ('Введите число: ')

# n = int (input ())

# count = 1

# for i in range (0, n - 1):
#     print (f"{count}", end = ', ')
#     count = count * (-3)
# print (count)


# N = int(input('Введите значение N: '))
# def sequence(n):
#     for i in range(n):
#         print((-3) ** i, end=' ')
# sequence(N)

# N = int(input('N = '))
# lst1 = []
# for i in range(N + 1):
#     lst1.append(3 * i + 1)
# print(lst1)

# s1 = 'aa ab aba ewfwef'
# s2 = 'aba'
# some_str_1 = s1
# some_str_2 = s2
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
#     if some_str_1[i:i + len_str_2] == some_str_2:
#         count += 1
#     i += 1
# print(count)

# print('Введите первую строку: ')

# string_1 = input()

# print('Введите вторую строку: ')

# string_2 = input()

# count = 0

# for i in range(0, len(string_1) - 1):
#     text = string_1[i:i + len(string_2)]
#     if text == string_2:
#         count = count + 1
# print(count)
