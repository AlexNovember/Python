# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# arr = [2, 3, 5, 9, 3]
# print(sum(x for i, x in enumerate(arr) if i % 2 != 0))





# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i%1,2) for i in list if i%1 != 10]
# print(max(new_list) - min(new_list))





# 2* Напишите программу вычисления арифметического 
# выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, 
# меняющих приоритет операций.
#  *Пример:* 
#  1+2*3 => 7; 
# (1+2)*3 => 9;



# import re
 
 
# symbols = {
#   "^": lambda x, y: str(int(x)**int(y)),
#   "*": lambda x, y: str(int(x) * int(y)),
#   "/": lambda x, y: str(int(x) / int(y)),
#   "+": lambda x, y: str(int(x) + int(y)),
#   "-": lambda x, y: str(int(x) - int(y))
# }
 
# priority_symbols = r"\((.+?)\)"
# action_symbols = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
 
 
# def actions(expresion: str) -> str:
 
#     while (match := re.search(priority_symbols, expresion)):
#         expresion: str = expresion.replace(match.group(0), actions(match.group(1)))
 
#     for symbol, action in symbols.items():
#         while (match := re.search(action_symbols.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
#     return expresion
 
 
# exp = "(1+2)*3+4+(3*2)"
# print(actions(exp))