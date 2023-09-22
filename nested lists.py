# 1. Создать пустой вложенный список.
# 2. Добавить элемент во вложенный список.
# 3. Получить длину вложенного списка.
# nested_list = []
# nested_list.append([2, 4])
# nested_list.append([6, 10])
# print(len(nested_list))
# print(nested_list)

# 4. Извлечь элемент из вложенного списка по индексу
# print(nested_list[1])
# a = nested_list[1][1]
# print(a)

# 5. Заменить элемент во вложенном списке по индексу.
# nested_list[1][0] = 1
# print(nested_list)

# 6. Добавить новый вложенный список в основной список.
# nested_list.append([11, 12])
# print(nested_list)

# 7. Объединить два вложенных списка в один.
# nested_list = nested_list[0] + nested_list[1] + nested_list[2]
# print(nested_list)
nested_list = [[12, 4, 111], [111, 10], [11, 12, 111], [11, 12]]
print(nested_list)
# new = []
# for lists in nested_list:
#     new.extend(lists)
# print(new)

# 8. Удалить вложенный список из основного списка.
# del_index = 1
# nested_list.pop(del_index)
# print(nested_list)

# 9. Создать копию вложенного списка.
# copy_nested_list = nested_list.copy()
# print(copy_nested_list)

# 10. Посчитать количество вложенных списков в основном списке.
# counter = 0
# for sublist in nested_list:
#     counter += 1
# print(counter)

# 11. Посчитать общее количество элементов во всех вложенных списках.
# counter = 0
# for sublists in nested_list:
#     for elem in sublists:
#         counter += 1
# print(counter)

# 12. Получить сумму всех чисел во всех вложенных списках.
# summa = 0
# for sublists in nested_list:
#     for elem in sublists:
#         if type(elem) == int:
#             summa += elem
# print(summa)

# 13. Найти наибольший элемент во всех вложенных списках.
# max_elem = float('-inf')
# for sublists in nested_list:
#     for elem in sublists:
#         if type(elem) == int:
#             if elem > max_elem:
#                 max_elem = elem
# print(max_elem)
# другое решение
# all_elements = [elem for sublist in nested_list for elem in sublist]
# max_elem = max(all_elements)
# print(max_elem)

# 14. Найти наименьший элемент во всех вложенных списках.
# all_elem = [elem for sublist in nested_list for elem in sublist]
# min_elem = min(all_elem)
# print(min_elem)

# 15. Сортировать вложенный список по возрастанию.
# for sublist in nested_list:
#     sublist.sort()
# print(nested_list)

# 16. Сортировать вложенный список по убыванию.
# for sublist in nested_list:
#     sublist.sort(reverse=True)
# print(nested_list)

# 17. Обратить порядок элементов во вложенном списке.
# for sublist in nested_list:
#     sublist.reverse()
# print(nested_list)

# 18. Удалить все дубликаты во вложенном списке.
# nested_list_2 = [[12, 4], [111, 10], [11, 12], [11, 12]]
# new_list = []
# for sublist in nested_list_2:
#     if sublist not in new_list:
#         new_list.append(sublist)
# print(new_list)

# 19. Проверить, существует ли определенный элемент во вложенном списке.
# def check_elem_in_nesterdlist(some_list: list, elem_to_find):
#     for sublist in nested_list:
#         if elem_to_find in sublist:
#             return True
#         else:
#             return False
# resalt = check_elem_in_nesterdlist(nested_list, elem_to_find='4')
# print(resalt)

# 20. Создать список из всех уникальных элементов во вложенных списках.
# list_out = []
# for sublist in nested_list:
#     for elem in sublist:
#         if elem not in list_out:
#             list_out.append(elem)
# print(list_out)

# 21. Посчитать количество четных чисел во вложенном списке.
# counter = 0
# for sublist in nested_list:
#     for elem in sublist:
#         if isinstance(elem, int):
#             if elem % 2 == 0:
#                 counter += 1
# print(counter)

# 22. Посчитать количество строк, длина которых больше 10 символов, во вложенном списке.
# nested_list_with_strings = [["apple", "banana", "cherry"], ["dog", "cat", "elephant"], ["red", "green", "blue"]]
# counter = 0
# for sublist in nested_list_with_strings:
#     for elem in sublist:
#         if len(elem) >= 6:
#             counter += 1
# print(counter)

# 23. Извлечь все числа из вложенных списков и объединить их в один список.
# nested_list_with_strings = [["apple", "banana", -11,  "cherry"], ["dog", "cat", -7,  "elephant"], ["red", 5, "green", "blue"]]
# list_out = []
# for sublist in nested_list_with_strings:
#     for elem in sublist:
#         if isinstance(elem, int):
#             list_out.append(elem)
# print(list_out)

# 24. Проверить, есть ли хотя бы одно положительное число во всех вложенных списках.
# nested_list_with_strings = [["apple", "banana", -11,  "cherry"], ["dog", "cat", -7,  "elephant"], ["red", 5, "green", "blue"]]
# found_positive = False
# for sublist in nested_list_with_strings:
#     for elem in sublist:
#         if isinstance(elem, int) and elem > 0:
#             found_positive = True
#             break  # Нашли положительное число, выходим из цикла
#     if found_positive:
#         break  # Нашли положительное число в одном из подсписков, выходим из внешнего цикла
# if found_positive:
#     print("Есть хотя бы одно положительное число во всех вложенных списках.")
# else:
#     print("Нет положительных чисел во всех вложенных списках.")

# 25. Создать список средних значений из каждого вложенного списка.
# aver = 0
# summa = 0
# list_out = []
# for sublist in nested_list:
#     for elem in sublist:
#         if isinstance(elem, int):
#             summa += elem
#             aver = summa / len(sublist)
#             list_out.append(aver)
# print(list_out)

# 26. Найти индекс первого вхождения определенного элемента во всех вложенных списках.
# list_to_work = [[12, 4, 111], [111, 10], [11, 12, 111], [111, 12]]
# list_out = []
# elem_to_find_index = 111
# for sublist in list_to_work:
#     index_found = False  # Флаг для отслеживания, был ли найден элемент в текущем подсписке
#     for index, elem in enumerate(sublist):
#         if elem == elem_to_find_index and not index_found:
#             list_out.append(index)
#             index_found = True  # Устанавливаем флаг, чтобы не добавлять повторные индексы
#     if not index_found:
#         list_out.append(None)  # Если элемент не найден в текущем подсписке, добавляем None
#
# print(list_out)

# # 27. Найти индекс последнего вхождения определенного элемента во всех вложенных списках.
# list_to_work = [[12, 4, 111], [111, 10], [11, 12, 111], [111, 12]]
# list_out = []
# elem_to_find_index = 111
#
# for sublist in list_to_work:
#     indices = [index for index, elem in enumerate(sublist) if elem == elem_to_find_index]
#     if indices:
#         last_index = indices[-1]  # Берем последний индекс из списка
#         list_out.append(last_index)
#     else:
#         list_out.append(None)  # Если элемент не найден, добавляем None
#
# print(list_out)

# 28. Создать новый вложенный список, в котором все элементы возведены в квадрат.
# list_out = [[elem ** 2 for elem in sublist if isinstance(elem, int)] for sublist in nested_list]
# print(list_out)

# 29. Удалить все пустые вложенные списки из основного списка.
# nested_list_3 = [[144, 16], [12321, 100], [121, 144], [], []]
# print(nested_list_3)
# list_out = []
# for sublist in nested_list_3:
#     if len(sublist) > 0:
#         list_out.append(sublist)
#         nested_list_3 = list_out
# print(nested_list_3)

# 30. Заменить все отрицательные числа во всех вложенных списках на нули.
# nested_list_4 = [[144, 16], [12321, -100], [121, 144], [-4, 28], [65]]
# list_out = []
# for sublist in nested_list_4:
#     for elem in sublist:
#         if isinstance(elem, int) and elem < 0:
#             elem = 0
#         list_out.append(elem)
#         nested_list_4 = list_out
# print(nested_list_4)

# 31. Сгенерировать новый вложенный список, состоящий из случайных чисел.
# import random
# list_generate = []
#
# for i in range(0, 3):# длина влооженного списка
#     sublist = []
#     for j in range(0, 3): # кол-во элементов в списке
#         random_num = random.randint(0, 100)
#         sublist.append(random_num)
#     list_generate.append(sublist)
# print(list_generate)

# 32. Создать новый вложенный список, в котором строки изначально были в обратном порядке.
# nested_list_to_replace = [["apple", "banana",  "cherry"], ["dog", "cat",   "elephant"], ["red",  "green", "blue"]]
# nested_list_out = []
# for sublist in nested_list_to_replace:
#     for elem in sublist:
#         nested_list_out.append(elem[::-1])
# print(nested_list_out)

# 33. Проверить, все ли вложенные списки имеют одинаковую длину.
# flag = True  # Предполагаем, что все списки имеют одинаковую длину
# first_length = len(nested_list[0]) # Получим длину первого вложенного списка
# for sublist in nested_list[1:]:
#     if len(sublist) != first_length:
#         flag = False  # Если длина не совпадает, устанавливаем флаг в False и выходим из цикла
#         break
# if flag:
#     print('+')
# else:
#     print('-')

# 34. Получить список индексов, где во всех вложенных списках присутствует определенный элемент.
# list_out = []
# elem_to_find_index = 111
# for sublist in nested_list:
#     for index, elem in enumerate(sublist):
#         if elem == elem_to_find_index:
#             list_out.append(index)
# print(list_out)

# 35. Создать список, в котором все элементы уникальны и отсортированы по возрастанию.
# list_out = []
# for sublist in nested_list:
#     for elem in sublist:
#         if elem not in list_out:
#             list_out.append(elem)
#             a = sorted(list_out)
# print(a)

# 36. Извлечь первые N элементов из каждого вложенного списка и создать новый список.
# nested_list_6 = [[144, 16, 'ttttt'], [12321, 'lime', -100], [121, 144, 'kiwi']]
# list_out = []
# first_length = len(nested_list_6[0])  # Получим длину первого вложенного списка
# flag = True
# for sublist in nested_list_6:
#     if len(sublist) != first_length:
#         flag = False
#         break  # Если хоть один вложенный список имеет другую длину, завершаем цикл
#     list_out.append(sublist[2])
#
# if flag:
#     print(list_out)
# else:
#     print("Не все вложенные списки имеют одинаковую длину.")

#37. Проверить, являются ли все элементы вложенного списка числами.
# flag = False
# for sublist in nested_list:
#     for elem in sublist:
#         if isinstance(elem, int):
#             flag = True
#         else:
#             flag = False
# if flag == True:
#     print('+')
# else:
#     print('-')

# 38. Сложить элементы с одинаковыми индексами из всех вложенных списков.
# list_to_sum = [[12, 4, 111], [111, 10, 10], [11, 12, 111], [11, 12, 110]]
# first_len = len(list_to_sum[0])
# list_out = [0] * first_len  # Инициализируем список нулями такой же длины, как первый вложенный список
# flag = True
# for sublist in list_to_sum:
#     if len(sublist) != first_len:
#         flag = False
#         raise ValueError('Списки разной длины!')
#
#     for index, elem in enumerate(sublist):
#         list_out[index] += elem
#
# if flag:
#     print(list_out)

# 39. Найти разницу между максимальным и минимальным элементами во всех вложенных списках.
# list_out = []
# for sublist in nested_list:
#     max_elem = float('-inf')
#     min_elem = float('inf')
#     result = 0
#     for elem in sublist:
#
#         if isinstance(elem, int):
#             if elem > max_elem:
#                 max_elem = elem
#             if elem < min_elem:
#                 min_elem = elem
#     result = max_elem - min_elem
#     list_out.append(result)
# print(list_out)

# 40. Удалить все элементы, которые не являются числами, из вложенных списков.
# nested_list_5 = [[144, 'apple'], ['12321', -100], ['121', 144], [-4, 28], [65]]
# list_out = []
# for sublist in nested_list_5:
#     for elem in sublist:
#         if not isinstance(elem, int):
#             list_out.append(elem)
#         nested_list_5 = list_out
# print(nested_list_5)