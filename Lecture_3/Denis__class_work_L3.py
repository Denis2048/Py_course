# a = [1, 7, 3, 9, 6 ,8, 6, 6]
# a.append(45)
# print(a)
# a.insert(2, 88)
# print(len(a))
# a.reverse()
# print(a)
# res = a.pop(0)
# print(a, res)
# a.remove(88)   # Удаляет по значению
# print(a)

# print(a.count(6))
# #a.clear()
# print(a)
# print(a.index(6))

# q = [1, 2, 3, 4, 5]
# print(q)
# q[2] = int(input("Введите любое число: "))
# print(q)
# q.pop()
# print(q,"\nlength is ->", len(q))

# q = [1, 2, 3, 5]
# for i in q:
#     print(i)

# li = []
# for i in range(int(input("-->"))):
#     li.append(int(input("-->")))
# print(li)

# a = [21, 9, 8, 10]      # Апгрейд в ДЗ.
# N= len(a)
# print(a)
#
# for i in range(N-1):
#     for j in range(N-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
# max, min, sum

# li = [1, 3, 5, 6]
# id(li)
# print(li)

### a = li[:3] - срез li[::2] - # C реверсом от начала до конца с шагом 2.

# Множества set type.
# s = {1, 3, 5, 8, 1}
# print(1 in s)
# s.update({1, 2, 6, 66})
# print(s)
# s.discard(6)
# print(s)

# li = [1, 2, 3, 5, 1, 2, 3]
# li = list(set(li))
# print(li)

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list_new = set(my_list)
# print(my_list_new)

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# new_my_list = my_list[::-1]
# print(new_my_list)

## list comprehension.
# li = [1, 2, 3, 4, 5]
# resList = []
# for v in li:
#     resList.append(v**2)
# print(li)
# print(resList)

# li = [1, 2, 3, 4, 5]
# resList = [v**2 for v in li]
# print(resList)

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resList = [v**2 for v in li if v%2 == 0]
# print(resList)

# numbers = [int(input("-->")) for i in\
#            range(int(input("n -->")))]
# print(numbers)

# li = input("x x x x-->")
# print(li.split(" "))

# li = [[1,2,3], [3,8,9], [9,8,7]]
# print(li[0])
# print(li[0][2])
# li = [[1,2,3], [3,8,9], [9,8,7]]
# li[0].append(33)
# print(li)

# Lab 3.2
# beatles = []
# beatles.append("John_Lennon")
# beatles.append("Paul_McCartney")
# beatles.append("George_Harrison")
# print(beatles)
# for i in range(2):
#     beatles.append(input("Add to list -->"))
# print(beatles)
# del beatles[3:5]
# print(beatles)
# beatles.insert(0, "Ringo Starr")
# print(beatles)

#
# import copy
# dd = copy.deepcopy()
