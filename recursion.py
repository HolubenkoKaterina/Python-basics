# Подсчет числа вхождений определенного значения во вложенных словарях
# def count_value_in_nested_dicts(d, target):
#     count = 0
#     for value in d.values():
#         if isinstance(value, dict):
#             count += count_value_in_nested_dicts(value, target)
#         elif value == target:
#             count += 1
#     return count
#
# nested_dict = {
#     'a': {'x': 1, 'y': 2},
#     'b': {'z': 1, 'w': 3},
#     'c': {'x': 1, 'y': 1}
# }
#
# target_value = 1
# result = count_value_in_nested_dicts(nested_dict, target_value)
# print(result)  # Выведет: 3
#
# Рекурсивная проверка, являются ли все ключи словаря четными числами
# def all_keys_even(d):
#     for key in d.keys():
#         if not isinstance(key, int) or key % 2 != 0:
#             return False
#     for value in d.values():
#         if isinstance(value, dict) and not all_keys_even(value):
#             return False
#     return True
#
# nested_dict = {
#     2: {},
#     4: {'a': 1, 'b': 2},
#     6: {'c': 3, 'd': 4}
# }
#
# result = all_keys_even(nested_dict)
# print(result)  # Выведет: True
#
# Поиск всех ключей, состоящих из одной буквы, во вложенных словарях
# def find_single_letter_keys(d):
#     single_letter_keys = []
#     for key in d.keys():
#         if isinstance(key, str) and len(key) == 1:
#             single_letter_keys.append(key)
#         if isinstance(d[key], dict):
#             single_letter_keys.extend(find_single_letter_keys(d[key]))
#     return single_letter_keys
#
# nested_dict = {
#     'a': {'x': 1, 'y': 2},
#     'b': {'z': 1, 'w': 3},
#     'c': {'d': 1, 'e': 1}
# }
#
# result = find_single_letter_keys(nested_dict)
# print(result)  # Выведет: ['a', 'b', 'c', 'd', 'e']
#
# Рекурсивное суммирование всех значений в словаре, умноженных на их длины
# def recursive_sum_multiply(d):
#     total_sum = 0
#     for value in d.values():
#         if isinstance(value, dict):
#             total_sum += recursive_sum_multiply(value)
#         elif isinstance(value, (int, float)):
#             total_sum += value * len(str(value))
#     return total_sum
#
# nested_dict = {
#     'a': {'x': 1, 'y': 2},
#     'b': {'z': 1, 'w': 3},
#     'c': {'x': 1, 'y': 1.5}
# }
#
# result = recursive_sum_multiply(nested_dict)
# print(result)  # Выведет: 23.5