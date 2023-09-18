# 1. Найти сумму всех элементов в списке.
# my_list = [10, 25, 7, -3, 42, 8]
# def sum_elem(some_list):
#     summa = 0
#     for elem in some_list:
#         if type(elem) == int:
#             summa += elem
#     return f'{summa} сумма элементов в списке {some_list}'
# result = sum_elem(my_list)
# print(result)

# 2. Найти среднее значение элементов в списке.
# my_list = [10, 25, 7, -3, 42, 8]
# def aver_elem(some_list):
#     summa = 0
#     for elem in some_list:
#         if type(elem) == int:
#             summa += elem
#             aver = round(summa / len(some_list), 2)
#             return f'{aver} среднее значение элемента \n в списке {some_list}'
# result = aver_elem(my_list)
# print(result)

# 3. Найти минимальный элемент в списке.
# my_list = [10, 25, 7, -3, 42, 8]
# def min_elem(some_list: list):
#     min_num = float('inf') # установим его по умолчания как неизвестная бесконечность
#     for elem in some_list:
#         if type(elem) == int:
#             if elem < min_num:
#                 min_num = elem
#     return min_num
# result = min_elem(my_list)
# print(result)

# 4. Найти максимальный элемент в списке.
# my_list = [10, 25, 7, -3, 42, 8]
# def max_elem(some_list):
#     max_elem = float('-inf')
#     for elem in some_list:
#         if type(elem) == int:
#             if max_elem < elem:
#                 max_elem = elem
#     return max_elem
# result = max_elem(my_list)
# print(result)
# другой вариант решения
# my_list = [10, 25, 7, -3, 42, 8]
# def max_elem(some_list):
#     max_el = some_list[0]
#     for elem in some_list:
#         if max_el < elem:
#             max_el = elem
#     return max_el
# resalt = max_elem(my_list)
# print(resalt)

# 5. Посчитать количество элементов в списке.
# my_list = [10, 25, 7, -3, 42, 8]
# def lenght_list(some_list):
#     return len(some_list)
# resalt = lenght_list(my_list)
# print(resalt)

# 6. Отсортировать элементы списка в порядке возрастания.
# my_list = [10, 25, 7, -3, 42, 8]
# def sorted_list(some_list: list):
#
#     out = sorted(my_list)
#     return out
# resalt = sorted(my_list)
# print(resalt)

# 7. Отсортировать элементы списка в порядке убывания.
# my_list = [10, 25, 7, -3, 42, 8]
# def sorted_list(some_list: list):
#     out = sorted(some_list, reverse=True)
#     return out
# resalt = sorted_list(my_list)
# print(resalt)

# 8. Удалить все дубликаты из списка.
# my_list = [10, 25, 25, 7, -3, 42, 8, 8]
# def del_duplicates(some_list: list):
#     list_out = []
#     for elem in some_list:
#         if elem not in list_out:
#             list_out.append(elem)
#     return list_out
# resalt = del_duplicates(my_list)
# print(resalt)

# 9. Найти сумму элементов на четных позициях списка.
# my_list = [10, 25, 25, 7, -3, 42, 8, 8]
# def summa_even_index(some_list):
#     summa = 0
#     for index, elem in enumerate(some_list):
#         if index % 2 == 0:
#             summa += elem
#     return summa
# resalt = summa_even_index(my_list)
# print(resalt)

#другой вариант решения
# my_list = [10, 25, 25, 7, -3, 42, 8, 8]
# def summa_even_index(some_list):
#     summa = 0
#     for index in range(0, len(some_list), 2):
#         summa += some_list[index]
#     return summa
# resalt = summa_even_index(my_list)
# print(resalt)

# 10. Найти сумму элементов на нечетных позициях списка.
# my_list = [10, 25, 25, 7, -3, 42, 8, 8]
# def summa_even_index(some_list):
#     summa = 0
#     for index, elem in enumerate(some_list):
#         if index % 2 != 0:
#             summa += elem
#     return summa
# resalt = summa_even_index(my_list)
# print(resalt)
#другой вариант решения
# my_list = [10, 25, 25, 7, -3, 42, 8, 8]
# def summa_even_index(some_list):
#     summa = 0
#     for index in range(1, len(some_list), 2):
#         summa += some_list[index]
#     return summa
# resalt = summa_even_index(my_list)
# print(resalt)

# 11. Заменить все отрицательные элементы на нули.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8]
# def change_negative_number_to_zero(some_list):
#     for index, elem in enumerate(some_list):
#         if elem < 0:
#             some_list[index] = 0
#     return some_list
#
# resalt = change_negative_number_to_zero(my_list)
# print(resalt)

#другой вариант решения
# my_list = [10, 25, 25, 7, -3, 42, -8, 8]
# def change_negative_number_to_zero(some_list: list):
#     for index in range(len(some_list)):
#         if some_list[index] < 0:
#             some_list[index] = 0
#     return some_list
# resalt = change_negative_number_to_zero(my_list)
# print(resalt)

# 12. Поменять местами первый и последний элементы списка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8]
# def change_place(some_list):
#     some_list[0], some_list[-1] = some_list[-1], some_list[0]
#     return some_list
# resalt = change_place(my_list)
# print(resalt)

# 13. Удалить элемент с определенным значением из списка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def delete_elem_some_value(some_list: list, element):
#     while element in some_list:
#         some_list.remove(element)
#     return some_list
# resalt = delete_elem_some_value(my_list, element=-3)
# print(resalt)

#другой вуариант решения
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def delete_elem_some_value(some_list: list, element_to_delete):
#     new_list = [el for el in some_list if el != element_to_delete]
#     return new_list
# resalt = delete_elem_some_value(my_list, element_to_delete=-3)
# print(resalt)

# 14. Подсчитать количество элементов, удовлетворяющих определенному условию.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def delete_elem_some_value(some_list: list, element):
#     counter = 0
#     for elem in some_list:
#         if element == elem:
#             counter += 1
#     return counter
# resalt = delete_elem_some_value(my_list, element=8)
# print(resalt)

# 15. Найти индекс первого вхождения элемента в список.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def find_index_for_element(some_list: list, elem):
#     for index, element in enumerate(some_list):
#         if elem == element:
#             return index
# resalt = find_index_for_element(my_list, elem=-3)
# print(resalt)

# 16. Найти индекс последнего вхождения элемента в список.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3, 18]
# def find_last_index_element(some_list: list, element_to_find: int):
#     last_index = -1
#     for index, el in enumerate(some_list):
#         if el == element_to_find:
#             last_index = index
#     return last_index
# resalt = find_last_index_element(my_list, element_to_find=-3)
# print(resalt)

# 17. Перевернуть список в обратном порядке.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def reverse_list(some_list: list):
#     some_list = some_list[::-1]
#     return some_list
# resalt = reverse_list(my_list)
# print(resalt)

# 18. Скопировать список.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3, -3]
# new_list = my_list.copy()
# print(new_list)

# 19. Объединить два списка в один.
# list1 = [2, 4, 3, 15]
# list2 = [12, 14, 13, 25, 36]
# list_out = list1+list2
# print(list_out)

# 21. Найти моду списка (самый часто встречающийся элемент).
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3, -3]
# def find_most_common_element(some_list: list):
#     element_count = {}  # Создаем словарь для подсчета количества вхождений каждого элемента
#
#     for el in some_list:
#         if el in element_count:
#             element_count[el] += 1
#         else:
#             element_count[el] = 1
#
#     most_common_element = None
#     max_count = 0
#
#     for el, count in element_count.items():
#         if count > max_count:
#             most_common_element = el
#             max_count = count
#
#     return most_common_element
# resalt = find_most_common_element(my_list)
# print(resalt)

# 22. Удалить все элементы, которые делятся на заданное число без остатка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def del_elem_divide_elem(some_list: list, divider: int):
#     list_out = [elem for elem in some_list if elem % divider != 0]
#     return list_out
# resalt = del_elem_divide_elem(my_list, divider=3)
# print(resalt)

# 23. Проверить, является ли список палиндромом (читается одинаково слева направо и справа налево).
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def check_palindrom(some_list: list):
#     if some_list == some_list[::-1]:
#         return 'да, это палиндромом'
#     else:
#         return 'нет, это не палиндромом'
# resalt = check_palindrom(my_list)
# print(resalt)

# 24. Подсчитать количество элементов, больших/меньших определенного значения.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def find_elem(some_list: list, value: int):
#     counter_more_value = 0
#     counter_less_value = 0
#     for elem in some_list:
#         if elem > value:
#             counter_more_value += 1
#         else:
#             counter_less_value += 1
#     return counter_more_value, counter_less_value
# resalt = find_elem(my_list, value=43)
# print(resalt)

# 25. Заменить все элементы списка на определенное значение.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def change_elem_on_value(some_list: list, value: int):
#     for index in range(len(some_list)):
#         some_list[index] = value
#     return some_list
# resalt = change_elem_on_value(my_list, value=2)
# print(resalt)

# 26. Создать новый список, содержащий только уникальные элементы исходного списка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_uniq_elem(some_list: list):
#     list_out = []
#     for elem in some_list:
#         if elem not in list_out:
#             list_out.append(elem)
#     return list_out
# resalt = get_uniq_elem(my_list)
# print(resalt)

# 27. Разделить список на два списка: четные и нечетные элементы.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_list_jdd_even_numb(some_list: list):
#     even_list_numb = []
#     odd_list_numb = []
#     for elem in some_list:
#         if elem % 2 == 0:
#             even_list_numb.append(elem)
#         else:
#             odd_list_numb.append(elem)
#     return f'{even_list_numb} список четных элементов, \n{odd_list_numb} список нечетных элементов'
# resalt = get_list_jdd_even_numb(my_list)
# print(resalt)

# 28. Найти разницу между соседними элементами списка.

# # 29. Вычислить сумму элементов в списке, находящихся между минимальным и максимальным элементами.
# my_list = [10, -35, 25, 7, -3, 42, -8, 8, -3]
# def summa_between_max_min_elem(some_list: list):
#     max_el = float('-inf')
#     min_el = float('inf')
#     sum_between = 0
#     for index, elem in enumerate(some_list):
#         if elem > max_el:
#             max_el = elem
#         if elem < min_el:
#             min_el = elem
#         min_index = some_list.index(min_el)
#         max_index = some_list.index(max_el)
#
#         # Определяем начальный и конечный индексы для суммирования
#         start_index = min(min_index, max_index) + 1
#         end_index = max(min_index, max_index)
#
#         # Суммируем элементы между минимальным и максимальным элементами
#         sum_between = sum(some_list[start_index:end_index])
#
#     return sum_between
#
# result = summa_between_max_min_elem(my_list)
# print(result)


# 30. Посчитать сумму квадратов элементов списка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_square_elem(some_elem: list):
#     list_square = [elem ** elem for elem in some_elem]
#     return list_square
# resalt = get_square_elem(my_list)
# print(resalt)

# 31. Увеличить каждый элемент списка на заданное число.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_new_list_plus_number(some_list: list, number_to_sum: int):
#     new_list = [elem + number_to_sum for elem in some_list]
#     return new_list
# resalt = get_new_list_plus_number(my_list, number_to_sum=4)
# print(resalt)
# другое решение
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_new_list_plus_number(some_list: list, number_to_sum: int):
#     new_list = []
#     for elem in some_list:
#         new_list.append(elem + number_to_sum)
#     return new_list
# resalt = get_new_list_plus_number(my_list, number_to_sum=4)
# print(resalt)

# 32. Проверить, содержит ли список элементы в заданном диапазоне.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def check_range_elem(some_list: list, start: int, finish: int):
#     for elem in some_list:
#         if elem in range(start, finish +1):
#             return True
#         else:
#             return False
# resalt = check_range_elem(my_list, start=2, finish=4)
# print(resalt)

# 33. Вычислить произведение всех элементов списка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def mult(some_list: list):
#     multi = 1
#     for elem in some_list:
#         multi *= elem
#     return multi
# resalt = mult(my_list)
# print(resalt)

# 34. Удалить все элементы списка, кратные заданному числу.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def del_el_multiples_number(some_list: list, elem_multiplace: int):
#     list_out = [el for el in some_list if el % elem_multiplace != 0]
#     return list_out
# resalt = del_el_multiples_number(my_list, elem_multiplace=5)
# print(resalt)

# 35. Оставить только элементы, находящиеся на четных позициях.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_even_index_number(some_list: list):
#     list_out = [elem for index, elem in enumerate(some_list) if index % 2 == 0]
#     return list_out
# resalt = get_even_index_number(my_list)
# print(resalt)

# 36. Оставить только элементы, удовлетворяющие определенному условию (например, больше 10).
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def get_elem(some_list: list, num: int):
#     list_out = [elem for elem in some_list if elem > num]
#     return list_out
# resalt = get_elem(my_list, num=10)
# print(resalt)

# 37. Сложить соответствующие элементы двух списков и создать новый список с результатами.
# list_1 = [2, 4, 16, 18]
# list_2 = [12, 14, 26, 28]
# def summa_lists(lst_1:list, lst_2: list):
#     list_out = []
#     for index in range(len(lst_1)):
#         list_out.append(lst_1[index] + lst_2[index])
#     return list_out
# resalt = summa_lists(list_1, list_2)
# print(resalt)

# 38. Вычислить сумму всех положительных и отрицательных элементов списка отдельно.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def positive_negative_summa(some_list: list):
#     negative_num_summa = 0
#     positive_num_summa = 0
#     for elem in some_list:
#         if elem > 0:
#             positive_num_summa += elem
#         else:
#             negative_num_summa += elem
#     return f' сумма положительных чисел {positive_num_summa}, сумма отрицательных чисел {negative_num_summa}'
# resalt = positive_negative_summa(my_list)
# print(resalt)

# 39. Посчитать количество элементов, которые больше среднего значения списка.
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3]
# def counter_elem_then_aver(some_list: list):
#     summa = 0
#     counter = 0
#     for elem in some_list:
#         summa += elem
#     aver = round(summa / len(some_list), 2)
#     for elem in some_list: # с таким отступом среднее значение не включается в расчет
#         if elem > aver:
#             counter += 1
#     return counter, aver
#
#
# result = counter_elem_then_aver(my_list)
# print(result)

# 40. Найти наименьший нечетный элемент в списке.
# my_list = [10, 25, -25, 7, -3, 42, -8, 8, -13]
# def min_odd_number(some_list: list):
#     min_num = float('inf')
#     for elem in some_list:
#         if elem % 2 != 0:
#             if elem < min_num:
#                 min_num = elem
#     return min_num
# resalt = min_odd_number(my_list)
# print(resalt)
