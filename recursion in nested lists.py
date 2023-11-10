import random
nested_list = []
nested_lists = random.randint(1, 5)
for i in range(nested_lists):
    inner_list = []
    nums_in_inner_list = random.randint(1, 6)
    for j in range(nums_in_inner_list):
        inner_list.append(random.randint(1, 15))
    nested_list.append(inner_list)
print(nested_list)

# Рекурсивно вычислить сумму всех элементов во вложенных списках.
# def summa_all_elem_in_nested_list(some_nested_list: list):
#     summa = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             summa += summa_all_elem_in_nested_list(elem)
#         else:
#             summa += elem
#     return summa
# print(summa_all_elem_in_nested_list(nested_list))

# Рекурсивно найти наибольший элемент во вложенных списках.
# def find_max_elem_in_nested_list(some_nested_list: list):
#     max_elem = float('-inf')
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             max_elem_nested_list = find_max_elem_in_nested_list(elem)
#             if max_elem_nested_list > max_elem:
#                 max_elem = max_elem_nested_list
#         elif elem > max_elem:
#             max_elem = elem
#     return max_elem
# print(find_max_elem_in_nested_list(nested_list))

# Рекурсивно найти наименьший элемент во вложенных списках.
# def find_min_elem_in_nested_list(some_nested_list: list):
#     min_elem = float('inf')
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             min_elem_nested = find_min_elem_in_nested_list(elem)
#             if min_elem_nested < min_elem:
#                 min_elem = min_elem_nested
#         elif elem < min_elem:
#             min_elem = elem
#     return min_elem
# print(find_min_elem_in_nested_list(nested_list))

# Рекурсивно найти среднее значение всех чисел во вложенных списках.
# def find_aver_in_nested_list(some_nested_list: list):
#     summa = 0
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             summa_nested, counter_nested = find_aver_in_nested_list(elem)
#             summa += summa_nested
#             counter += counter_nested
#         else:
#             summa += elem
#             counter += 1
#     aver = summa / counter if counter > 0 else 0
#     return summa, counter
#
# summa, counter = find_aver_in_nested_list(nested_list)
# aver = summa / counter if counter > 0 else 0
# print(aver)

# Рекурсивно вычислить произведение всех элементов во вложенных списках.
# def multiplace_elem_in_nested_list(some_nested_list: list):
#     mult = 1
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             mult *= multiplace_elem_in_nested_list(elem)
#         else:
#             mult *= elem
#     return mult
# print(multiplace_elem_in_nested_list(nested_list))

# Рекурсивно найти количество списков внутри списка.
# def find_counter_nested_list(some_nested_list: list):
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             counter += find_counter_nested_list(elem)
#             counter += 1
#
#     return counter
# print(find_counter_nested_list(nested_list))

# Рекурсивно найти сумму всех четных элементов во вложенных списках.
# def summa_even_elem_in_nested_list(some_nested_list: list):
#     summa = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             summa += summa_even_elem_in_nested_list(elem)
#         elif elem % 2 == 0:
#             summa += elem
#     return summa
# print(summa_even_elem_in_nested_list(nested_list))

# Рекурсивно найти сумму всех нечетных элементов во вложенных списках.
# def find_summa_odd_elem_in_nested_list(some_nested_list: list):
#     summa = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             summa += find_summa_odd_elem_in_nested_list(elem)
#         elif elem % 2 != 0:
#             summa += elem
#     return summa
# print(find_summa_odd_elem_in_nested_list(nested_list))

# Рекурсивно найти сумму элементов на четных позициях во вложенных списках.
# def find_summa_elem_on_even_index(some_nested_list: list):
#     summa = 0
#     for index, elem in enumerate(some_nested_list):
#         if isinstance(elem, list):
#             summa += find_summa_elem_on_even_index(elem)
#         elif index % 2 == 0:
#             summa += elem
#     return summa
# print(find_summa_elem_on_even_index(nested_list))

# Рекурсивно найти сумму элементов на нечетных позициях во вложенных списках.
# def summa_elem_on_odd_index(some_nested_list: list):
#     summa = 0
#     for index, elem in enumerate(some_nested_list):
#         if isinstance(elem, list):
#             summa += summa_elem_on_odd_index(elem)
#         elif index % 2 != 0:
#             summa += elem
#     return summa
# print(summa_elem_on_odd_index(nested_list))

# Рекурсивно найти количество списков, содержащих заданное значение.
# def find_counter_inner_lists_on_value(nested_list: list, value_find):
#     counter = 0
#     for elem in nested_list:
#         if isinstance(elem, list):
#             counter += find_counter_inner_lists_on_value(elem, value_find)
#         elif elem == value_find:
#             counter += 1
#     return counter
# print(find_counter_inner_lists_on_value(nested_list, value_find=72))

# Рекурсивно найти все списки, содержащие заданное значение.
# def find_lists_with_value(some_nested_list: list, value_find):
#     lists = []
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             sublists = find_lists_with_value(elem, value_find)
#             lists.extend(sublists)
#         elif value_find == elem:
#             lists.append(some_nested_list)
#             break  # Мы нашли значение, не нужно продолжать поиск в этом подсписке
#     return lists
#
# print(find_lists_with_value(nested_list, value_find=13))

# Рекурсивно объединить все списки внутри списка в один общий список.
# def union_sublists(some_nested_list: list):
#     list_out = []
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             subl = union_sublists(elem)
#             list_out.extend(subl)
#         else:
#             list_out.append(elem)
#     return list_out
# print(union_sublists(nested_list))

# Рекурсивно найти количество списков, в которых все элементы положительные.
# def count_nested_lists_all_positive_elem(some_nested_list: list):
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             if all(x > 0 for x in elem):
#                 counter += 1
#             counter += count_nested_lists_all_positive_elem(elem)
#     return counter
# print(count_nested_lists_all_positive_elem(nested_list))

# Рекурсивно найти максимальную глубину вложенности списка.
# def find_max_depth_nested_list(some_nested_list: list):
#     max_depth = 1
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             depth_inner = 1 + find_max_depth_nested_list(elem)
#             if depth_inner > max_depth:
#                 max_depth = depth_inner
#     return max_depth
# print(find_max_depth_nested_list(nested_list))

# Рекурсивно проверить, все ли элементы во вложенных списках являются числами.
# def check_element_in_nested_list(some_nested_list: list, type_elem):
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             subl = check_element_in_nested_list(elem, type_elem)
#             if not all(type(el) == int for el in elem):
#                 return False
#
#         elif type(elem) != int:
#             return False
#
#     return True
# nested_list1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [4, 11, 12]]
# print(nested_list1)
# print(check_element_in_nested_list(nested_list1, type_elem='int'))

# Рекурсивно найдите количество списков, в котором бы на один элемент больше заданного числа.
# def count_sublist_with_element_upper_value(some_nested_list: list, value_find):
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             counter_inner = count_sublist_with_element_upper_value(elem, value_find)
#             if counter_inner > 0:
#                 counter += 1
#         elif elem > value_find:
#             counter += 1
#
#     return counter
# print(count_sublist_with_element_upper_value(nested_list, value_find=11))

# Рекурсивно найти количество списков, в которых все элементы четные.
# def find_count_nested_lists_with_positive_nums(some_nested_list: list):
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             counter += find_count_nested_lists_with_positive_nums(elem)
#         elif elem % 2 == 0:
#             counter += 1
#     return counter
# print(find_count_nested_lists_with_positive_nums(nested_list))

