# 1.Напишите программу, которая находит второе наименьшее число в списке
# some_list = [4, 15, -28, 0]
# def find_min_value(s_list: list):
#     new_list = sorted(s_list)
#     min_second_numb = new_list[1]
#     return f'{min_second_numb} второе наименьшее число в списке {s_list}'
# result = find_min_value(some_list)
# print(result)

# # 2.Напишите программу, которая находит разность между суммой элементов на четных позициях и суммой элементов на нечетных позициях в списке.
# some_list = [4, 15, -28, 0]
# def find_difference_sum_even_odd_positions(my_list: list):
#     sum_even_index = 0
#     sum_odd_index = 0
#
#     for index, elem in enumerate(my_list):
#         if index % 2 == 0:
#             sum_even_index += elem
#         else:
#             sum_odd_index += elem
#     result = sum_even_index - sum_odd_index
#     return result
# result = find_difference_sum_even_odd_positions(some_list)
# print(result)


# 3.Напишите программу, которая находит сумму элементов списка, находящихся между двумя заданными индексами.
# some_list = [4, 15, -28, 0]
# def summa_between_indexes(my_list: list, index1: int, index2: int):
#     summa = 0
#     for index in range(index1, index2 + 1):
#         summa += my_list[index]
#     return summa
# result = summa_between_indexes(some_list, index1=1, index2=3)
# print(result)

# 4.Напишите программу, которая находит количество элементов в списке, которые больше среднего значения всех элементов.
# some_list = [4, 15, -28, 0]
# def number(my_list):
#     aver = 0
#     summa = 0
#     counter = 0
#     for elem in my_list:
#         if type(elem) == int:
#             summa += elem
#             aver = summa / len(my_list)
#             if elem > aver:
#                 counter += 1
#     return f'{aver} это среднее значение, {counter} шт это кол-во элементов которые больше чем {aver}'
# result = number(some_list)
# print(result)

# 5.Напишите программу, которая находит сумму элементов на нечетных позициях, но только если элемент больше предыдущего.
# some_list = [4, 15, -28, 0]
#
# def sum_odd_position(my_list):
#     summa = 0
#     for index in range(1, len(my_list), 2):
#         if my_list[index] > my_list[index - 1]:
#             summa += my_list[index]
#     return summa
#
# result = sum_odd_position(some_list)
# print(result)


