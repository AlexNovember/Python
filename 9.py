list = [1, 2, 3, 6]
        # 0 1 2 3   
print(list[4 - 1])


# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range (1, 39) if i % 2 == 0]

# print(list)


# items = list(map(int, input().split()))
# print(*items)




# lst = []
 
# for x in range(-2, 7):
#     if x % 2 == 0:
#         lst.append(x * x)
 
 
# print(lst)
 
# lst1 = [x * x for x in range(-2, 7) if x % 2 == 0]
 
# print(lst1)


# allnumb = list(range(2, 11)) #Создаем список от 2 до 10.
# numb = [2, 5, 9, 8, 3, 7, 4, 10] #Список чисел от 2 до 10, но без 1 числа.
# a = sum(allnumb) #Складываем все значения списка чисел от 2 до 10.
# b = sum(numb) #Складываем все значения списка чисел от 2 до 10, но без одного числа.
# c = (a - b) 
# print (c)

# with open('1.txt', 'r') as f:
#     a = f.readlines()
#     print(a)


# with open("text.txt", "r") as f:
#     lst = list(map(int, f.read().split()))
# res = 0
# for key, item in enumerate(lst):
#     if key + 1 < len(lst) and item + 1 != lst[key + 1]:
#         res = item + 1
    
# print(res)



# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")

# txt = ("ываабв лповап абвцукв алоабвабв ываываыв")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

# nums = [1, 5, 2, 3, 4, 6, 1, 7]

# Первый вариант

# def pop(nums):
#     up = [nums[0]]
#     for i in nums:
#         if i > max(up):
#             up.append(i)
#     return up
    
# print(pop(nums))

# Второй вариант

# def get_up(nums):
#     ups = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
#             ups.append(nums[i])
#     return ups

# print(get_up(nums))

# array = [1, 5, 2, 3, 4, 6, 1, 7]

# for i in range(len(array)):
#     arr_n = [1]
#     arr_n[0] = array[0]
#     for j in range(i, len(array)):
#         if array[j] > arr_n[-1]:
#             arr_n.append(array[j])

#     print(arr_n)


# X = [6, 1, 3, 4, 9, -1, 1, 0, 19]
 
# L = []
# M = []
# j = 1
 
# while j < len(X):
#   i = j
#   N = X[:]
#   while i < len(N)-1:
#     if N[i] < N[i+1]: 
#       M.append(N[i])
#       i += 1
#     else:
#       N.pop(i+1)
      
#   j+=1
#   if len(L) < len(M):
#     L = M
#   M=[]
 
# if X[-1] > L[-1]:
#   L.append(X[-1])
  
# if X[0] < L[0]:
#   L.insert(0, X[0])
  
# print(L)
 
#[1, 3, 4, 9, 19]


# import numpy as np
 
# def is_inc(sequence):
#     return np.all(np.diff(sequence) > 0)
 
# def max_inc(sequence):
#     if is_inc(sequence):
#         return sequence
 
#     subs = [np.delete(sequence, i) for i in range(len(sequence))]
 
#     results_sub = [max_inc(sub) for sub in subs]
#     result = max(results_sub, key=lambda s: len(s))
#     return result
 
# # seq = np.array([4,5,6,0,1,7,2,8])
# seq = np.array([3, 1, 6, 8 ,9, -1, 1, 0, 19])
# print(max_inc(seq))