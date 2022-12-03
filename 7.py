# with open("test", "a") as file:

# # file.write(f"sdfljsd;fjs;dlfsfs\n")
# # file.write("2222222222222222222222222\n")
#     print(file.read())
#     print(file.readline())

# # file.close()

# 1. Задайте строку из набора чисел. Напишите программу,
#     которая покажет большее и меньшее число.
#     В качестве символа-разделителя используйте пробел.


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     С помощью математических формул нахождения корней квадратного уравнения

#     solve(a, b, c)

# 3. Задайте два числа. Напишите программу, которая найдёт НОК
#    (наименьшее общее кратное) этих двух чисел.

# str_ = sorted(map(int, input().split()))
# # print(str_)
# for index in range (len(str_)):
#     str_[index] = int (str_[index])
# print(max(str_),min(str_), sep = ' ')

# str_ = '43 25 56 54 121'.split()
# for index in range(len(str_)):
#     str_[index] = int(str_[index])

# print(max(str_),min(str_), sep = ' ')


# lst = [int(item) for item in "14 55 66".split(" ")]
# print(f"max: {max(lst)}\nmin: {min(lst)}")


def nod(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
 
 
x = int(input('a = '))
y = int(input('b = '))
print('Наименьшее общее кратное:', nod(x, y))
    
# a, b = 3, 7
# maxx = max(a, b)
# i = maxx
# while True:
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break
#     i += maxx
