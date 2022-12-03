# b = 22


# def f():
#     b = 55

#     def f_():
#         nonlocal b
#         b = 44


# print(b)
# f()
# print(b)


# from time import time
# print(str(time())[-1])

# from time import time

# def randfromtime(max):
#     time1 = time()
#     time1 = (time1 - int(time1))
#     return int(time1 * max)

# print(randfromtime(100))




# a = ["55", "uh", "6"]

# def f(l, n):
#     for item in l:
#         if item.isdigit():
#             if int(item) == n:
#                 return True
#     return False

# print(f(a, 55))


# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe", "asd"] #, ищем: "qwe", ответ: 3
# list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
# list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
# list4 = ["123", "234", 123, "567"] #, ищем: "123", ответ: -1
# list5 = [] #, ищем: "123", ответ: -1

# def find(l, item):
#     flag = False
#     for i in range(len(l)):
#         if l[i] == item:
#             if flag:
#                 return i
#             else:
#                 flag = True
#     return -1


# print(find(list1, 'qwe'))
# print(find(list2, 'йцу'))
# print(find(list3, 'йцу'))
# print(find(list4, '123'))
# print(find(list5, '123'))


from random import randint
import itertools

n = 55
    
mylist = ['22', '33', '123', 'fwefe', 'ytyy', '55']

def find_number(n, lst):
    return str(n) in lst

print(find_number(n, mylist))

