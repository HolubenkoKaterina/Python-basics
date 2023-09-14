# 1. Получите первый элемент списка.
# text = ['i like python.', ' i dont cry.']
# print(text[0][2])

# 2. Получите последний элемент списка.
#text = ['i like python.', ' i dont cry.', 55, '48']
# print(text[-1])

# 3. Получите элемент списка с индексом 3.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# print(text[3])

# 4. Получите элемент списка с индексом -2.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# print(text[-2])

# 5. Получите элемент списка с индексом 1 до 4 (не включая 4).
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# print(text[1:4])

# 6. Получите элемент списка с индексом 2 до конца списка.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# print(text[2::])

# 7. Получите элемент списка с индексом 0 до конца списка с шагом 2 (через один элемент).
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# print(text[0::2])

# 8. Измените значение элемента списка с индексом 2 на новое значение.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# change_element = 155
# text[2] = change_element
# print(text)

# 9. Измените значения элементов списка с индексами 0 и 1 на новые значения с помощью одной операции.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# change_element = [155, 156]
# text[0:2] = change_element
# print(text)

# 10. Получите первый элемент кортежа.
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# print(text[0])

# 11. Получите элемент кортежа с индексом 2.
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# print(text[2])

# 12. Получите элемент кортежа с индексом -1.
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# print(text[-1])

# 13. Получите элемент кортежа с индексом 1 до 3 (не включая 3).
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# print(text[1:3])

# 14. Получите элемент кортежа с индексом 0 до конца кортежа с шагом 2 (через один элемент).
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# print(text[::2])

# 15. Измените значение элемента кортежа с индексом 1 на новое значение..
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# text_new = list(text)
# change = 'i cry'
# text_new[1] = change
# print(tuple(text_new))

# 16. Измените значения элементов кортежа с индексами 0 и 2 на новые значения с помощью одной операции.
# text = ('i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa')
# text_new = list(text)
# change = 'i cry', 'cry i'
# text_new[0], text_new[2] = change
# print(tuple(text_new))

# 17. Получите элемент списка с индексом, который пользователь вводит с клавиатуры.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# index_interesting = int(input('введите ваш индекс..'))
# print(text[index_interesting])

# 18. Напишите программу, которая принимает на вход индекс и список, а затем выводит
# элемент списка с заданным индексом или сообщение об ошибке, если индекс выходит за пределы списка.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# index_interesting = int(input('введите ваш индекс..'))
# for index, element in enumerate(text):
#     flag = False
#     if index_interesting == index:
#         print(element)
#         flag = True
#         break
# if not flag:
#         print('нет такого элемента..')
# тут что то  подзабылось с флажком

# 19. Напишите программу, которая принимает на вход индексы и кортеж, а затем выводит
# элементы кортежа с заданными индексами или сообщение об ошибке, если индекс выходит за пределы кортежа.
# text = ['i like python.', ' i dont cry.', 55, '155, 14', '48', 'wiwa']
# index_interesting = int(input('введите ваш индекс..'))
# text = list(text)
# for index, element in enumerate(text):
#     flag = False
#     if index_interesting == index:
#         print(element)
#         flag = True
#         break
# if not flag:
#         print('нет такого элемента..')

# 20. Напишите программу, которая принимает на вход список чисел и выводит индекс первого
# отрицательного числа или сообщение, что отрицательных чисел нет.
# some_numbers = [4, 5, 15, 25, -55, 100, -100]
# for index, element in enumerate(some_numbers):
#     flag = False
#     if element < 0:
#         print(f'индекс первого отрицательного числа {index}')
#         flag = True
#         break
# if not flag:
#     print("нет отрицательных чисел в списке..")
