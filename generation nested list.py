import random

# nested_list = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
# print(nested_list)
#
# nested_list = []
# num_inner_lists = random.randint(1, 10)  # Генерация случайного числа от 1 до 10.
# for i in range(num_inner_lists):
#     inner_list = []
#     num_inner_elements = random.randint(1, 10)  # Генерация случайного числа от 1 до 10.
#
#     for j in range(num_inner_elements):
#         inner_list.append(random.randint(1, 100))  # Генерация случайного числа от 1 до 100.
#
#     nested_list.append(inner_list)
# print(nested_list)

# nested_list = []
# for i in range(3): #Этот цикл итерируется по значениям от 0 до 2 (включительно), создавая три внутренних списка.
#     inner_list = []
#     for j in range(3):# Вложенный цикл итерируется по значениям от 0 до 2 (включительно),
#         # создавая три числа в каждом внутреннем списке.
#         inner_list.append(i * 3 + j + 1)# можно так i + j*3 + 1
#     nested_list.append(inner_list)
# print(nested_list)
# nested_list = []

# for i in range(4):
#     inner_list = []
#     for j in range(3):
#         inner_list.append(random.randint(1, 100))
#     nested_list.append(inner_list)
# print(nested_list)

# nested_list = []
# num_inner_lists = random.randint(1, 20) # сколько вложеных списков сгенерируется
# for i in range(num_inner_lists):
#     inner_list = []
#     num_inner_elements = random.randint(1, 5)  # сколько элементов будет во внутреннем списке
#     for j in range(num_inner_elements):
#         inner_list.append(random.randint(1, 100))  # диапазон чисел
#     nested_list.append(inner_list)
# print(nested_list)