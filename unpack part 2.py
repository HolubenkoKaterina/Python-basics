
# Реализуйте функцию, которая принимает несколько строковых аргументов и возвращает объединенную строку с удаленными пробелами.
# sp = ['we like', 'he likes', 'she likes']
# def union_delete_probel(*args, sep=''):
#     result = sep.join(arg.replace(' ', '') for arg in args)
#     return result
# resalt = union_delete_probel(*sp)
# print(resalt)
#
# Напишите функцию, которая принимает неограниченное количество списков и объединяет их в один список.
# list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
# def union_lists_into_one(*args):
#     list_out = []
#     for elements in args:
#         for element in elements:
#             list_out.append(element)
#     return list_out
# resalt = union_lists_into_one(*list_of_lists)
# print(resalt)

# Создайте генератор, который возвращает все уникальные элементы из списка списков.
# list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
# def unique_elements_from_list(*args):
#     unique = set()
#     for inner_list in args:
#         for elem in inner_list:
#             unique.add(elem)
#     return list(unique)
# resalt = unique_elements_from_list(*list_of_lists)
# print(resalt)