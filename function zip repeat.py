# Создайте список из двух списков чисел и используйте zip, чтобы создать список пар чисел.
# import random
# my_list1 = [random.randint(5, 25) for _ in range(5)]
# my_list2 = [random.randint(5, 25) for  _ in range(5)]
# print(my_list1)
# print(my_list2)
# my_list3 = list(zip(my_list1, my_list2))
# print(my_list3)

# Используйте zip для объединения двух списков строк в список кортежей.
# list1 = ["apple", "banana", "cherry", "date"]
# list2 = ["orange", "grape", "kiwi", "plum"]
# list3 = list(zip(list1, list2))
# print(list3)

# Найдите среднее значение из двух списков чисел, используя zip.
# import random
# my_list1 = [random.randint(5, 25) for _ in range(5)]
# my_list2 = [random.randint(5, 25) for _ in range(5)]
# list_3 = list(zip(my_list1, my_list2))
# print(list_3)
# aver = 0
# summa = 0
# resalt = []
# for elem in list_3:
#     summa = elem[0] + elem[1]
#     aver = summa / 2
#     resalt.append(aver)
# print(resalt)

# Создайте новый список, состоящий из сумм элементов двух списков чисел, используя zip.
# import random
# my_list1 = [random.randint(5, 25) for _ in range(5)]
# my_list2 = [random.randint(5, 25) for _ in range(5)]
# list_3 = list(zip(my_list1, my_list2))
# print(list_3)
# resalt = [elem[0] + elem[1] for elem in list_3]
# print(resalt)

# Используйте zip, чтобы объединить список и его индексы в список кортежей.
# list1 = ["apple", "banana", "cherry", "date"]
# list_out = [(elem, index )for elem, index in enumerate(list1)]
# print(list_out)
# list1 = ["apple", "banana", "cherry", "date"]
# list_out = list(zip(list1, range(len(list1))))
# print(list_out)

# Создайте словарь из двух списков, один из которых содержит ключи, а другой - значения, с использованием zip.
# import random
# list1 = ["apple", "banana", "cherry", "date"]
# list2 = [random.randint(2, 11) for _ in range(4)]
# dict_out = {elem: elem2 for elem, elem2 in list(zip(list1, list2))}
# print(dict_out)

# Переверните пары элементов в списке кортежей, используя zip.
# import random
# my_list1 = [random.randint(5, 25) for _ in range(5)]
# my_list2 = [random.randint(5, 25) for _ in range(5)]
# list_3 = list(zip(my_list1, my_list2))
# print(list_3)
# list_out = [(elem[1], elem[0]) for elem in list_3]
# print(list_out)

# Используйте zip для соединения двух списков и создания нового списка строк.
# list1 = ["apple", "banana", "cherry", "date"]
# list2 = ["orange", "grape", "kiwi", "plum"]
# list3 = list(zip(list1, list2))
# list_out = [', '.join(elem) for elem in list3 ]
# print(list_out)

# Создайте два списка и используйте zip, чтобы создать список, содержащий строки вида "пара:
# (элемент из первого списка, элемент из второго списка)".
# list1 = ["apple", "banana", "cherry", "date"]
# list2 = ["orange", "grape", "kiwi", "plum"]
# list3 = list(zip(list1, list2))
# print(list3)