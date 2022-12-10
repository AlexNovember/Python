
# from random import randint
 
# CANDIES = 2022
# MAX_STEP = 28
 
# human = True
# cur_candies = CANDIES
 
 
# def get_ai_step():
#     return randint(1, min(MAX_STEP, cur_candies))
 
 
# def get_human_step():
#     while True:
#         cnt = input('Введите количество конфет: ')
#         if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
#             return int(cnt)
#         print('Введено некорректное значение')
 
 
# while cur_candies:
#     if human:
#         cur_candies -= get_human_step()
#     else:
#         cur_candies -= get_ai_step()
#     human = not human
 
# if human:
#     print('Победил БОТ')
# else:
#     print('Победил человек')




    
# from random import randint
 
# CANDIES = 60
# MAX_STEP = 28
 
# human = True
# cur_candies = CANDIES
 
 
# def get_ai_step():
#     return randint(1, min(MAX_STEP, cur_candies))
 
 
# def get_human_step():
#     while True:
#         cnt = input('Введите количество конфет: ')
#         if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
#             return int(cnt)
#         print('Введено некорректное значение')
 
 
# while cur_candies:
#     if human:
#         cnt = get_human_step()
#         cur_candies -= cnt
#         print(f'Пользователь взял {cnt} конфет. Осталось {cur_candies}.')
#     else:
#         cnt =get_ai_step()
#         cur_candies -= cnt
#         print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
#     human = not human
 
# if human:
#     print('Победил БОТ')
# else:
#     print('Победил человек')


# str_ = '10+5*1-50+6'

# lst = list(str.split('+', '-', '*', '/')) # получаем СПИСОК
# print(lst)
# temp = ' '.join(lst)
# print(temp)
# print(type(temp))

# lst = []
# last = -1
# for i, symbol in enumerate(str_):
#     if not symbol.isdigit():
#         lst.append(int(str_[last + 1:i]))
#         lst.append(symbol)
#         last = i
#     # print(i, symbol, lst, last)

# lst.append(int(str_[last + 1:i + 1]))
# print(lst)

# lst_1 = []
# if type(lst[0]) is int:
#     lst_1.append(lst[0]) 

# for i, symbol in enumerate(lst):
#     if symbol == "*":
#         lst_1[-1] = lst_1[-1] * lst[i + 1]
#     elif symbol == "/":
#         lst_1[-1] = lst_1[-1] / lst[i + 1]
#     elif symbol == "+":
#         lst_1.append(lst[i + 1])
#     elif symbol == "-":
#         lst_1.append(-lst[i + 1])

# print(sum(lst_1))


lst = []
last = -1
for i, symbol in enumerate(str_):
    if not symbol.isdigit():
        lst.append(int(str_[last + 
lst = []
last = -1
for i, symbol in enumerate(str_):
    if not symbol.isdigit():
        lst.append(int(str_[last + 1:i]))
        lst.append(symbol)
        last = i
    # print(i, symbol, lst, last)

lst.append(int(str_[last + 1:i + 1]))
print(lst)

lst_1 = []
if type(lst[0]) is int:
    lst_1.append(lst[0]) 

for i, symbol in enumerate(lst):
    if symbol == "*":
        lst_1[-1] = lst_1[-1] * lst[i + 1]
    elif symbol == "/":
        lst_1[-1] = lst_1[-1] / lst[i + 1]
    elif symbol == "+":
        lst_1.append(lst[i + 1])
    elif symbol == "-":
        lst_1.append(-lst[i + 1])

print(sum(lst_1))
