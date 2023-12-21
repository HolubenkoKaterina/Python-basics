# Откройте бинарный файл для чтения и выведите его содержимое.
# Запишите строку в бинарный файл.
# Прочитайте и выведите первые 10 байт из бинарного файла.
# text = 'i will learn python soon!'
# import pickle
# with open('binar_file.bin', 'wb') as my_file:
#     pickle.dump(text, my_file)
#
# try:
#     with open('binar_file.bin', 'rb') as my_file:
#         text = my_file.read(10)
#         print(text)
#
# except FileNotFoundError as error:
#     print(error)
#######################################################################################
# Создайте копию бинарного файла.
# import pickle
# try:
#     with open('binar_file.bin', 'rb') as my_file:
#         content = my_file.read()
# except FileNotFoundError as error:
#     print(error)
#
# with open('copy_binary_file', 'wb') as copy_file:
#     copy_file.write(content)
# # Замените определенный байт в бинарном файле на другое значение.
# with open('copy_binary_file', 'rb') as file_to_change:
#     content = bytearray(file_to_change.read())
#     byte_to_change_index = 5 # индекс байта который надо заменить
#     new_value_byte = b'\x55'
#     # Создаем новый массив байтов с заменой
#     new_content = content[:byte_to_change_index] + new_value_byte + content[byte_to_change_index + 1:]# тут все очень плоо(
#
# with open('copy_binary_file', 'bw') as my_file:
#     my_file.write(content)
#
# Посчитайте количество байтов в бинарном файле.
# try:
#     with open('copy_binary_file', 'rb') as my_file:
#         content = my_file.read()
#         count_bytes = len(content)
#         print("Количество байтов в файле:", count_bytes)
# except FileNotFoundError as error:
#     print(error)
###################################################################################
# Запишите список чисел в бинарный файл.
# import pickle
# with open('file_practice_again', 'wb') as my_file:
#     pickle.dump(list(range(0, 11)), my_file)
#
# # Считайте числа из бинарного файла и найдите их сумму.
# # Измените порядок байтов в бинарном файле на обратный.
# try:
#     with open('file_practice_again', 'rb') as file_read:
#         sum = 0
#         content = pickle.load(file_read)
#         print(f'{content} исходный список')
#         content_reverse = content[::-1]
#         print(f'{content}  список написаный в обратном порядке ')
#         for num in content:
#             sum += num
#         print(f'{sum} сумма чисел в файле')
#
# except FileNotFoundError as error:
#     print(error)
###############################################################################

# Создайте бинарный файл с определенным размером и заполните его нулями.
# file_size = 10  # размер файла в байтах
# with open('zero_filled_file.bin', 'wb') as my_file:
#     my_file.write(b'\x00' * file_size)
##########################################
# Запишите байты из двоичной строки в бинарный файл.
# numbers = list(range(0, 11))
# import struct
# import pickle
# with open('new_binary_file', 'wb') as my_file:
#     for num in numbers:
#         binary_file = struct.pack('i', num)
#         my_file.write(binary_file)
# # 'i' обозначает 4-байтовое целое число (integer) с знаком.
# # 'I': 4-байтовое целое число (беззнаковое).
# # 'h': 2-байтовое целое число (знаковое).
# # 'H': 2-байтовое целое число (беззнаковое).
# # 'f': 4-байтовое число с плавающей точкой (float).
# # 'd': 8-байтовое число с плавающей точкой (double).
#         my_file.write(binary_file)
#
# ########################################################################
# # Подсчитайте количество вхождений определенного байта в бинарном файле.
# target_byte = b'\x55'
# # try:
# with open('new_binary_file.bin', 'rb') as my_file:
#     content = my_file.read()
#     count = content.count(target_byte)
# print("Количество вхождений:", count)
#
# # except FileNotFoundError as error:
# #     print(error)
# #в этом задании почему то ошибка FileNotFoundError: [Errno 2] No such file or directory: 'new_binary_file.bin'
# #не знаю как исправить
