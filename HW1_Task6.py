"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое."""

from chardet import detect

WORD_1 = 'сетевое программирование'
WORD_2 = 'сокет'
WORD_3 = 'декоратор'

WORDS_LIST = [WORD_1, WORD_2, WORD_3]

with open('test_file.txt', 'w') as file_w:
    for el_str in WORDS_LIST:
        file_w.write(f'{el_str}\n')
file_w.close()


with open('test_file.txt', 'rb') as file_rb:
    values = file_rb.read()
ENCODING = detect(values)['encoding']
print(ENCODING)

with open('test_file.txt', 'r') as file_r:
    values = file_r.read()
print(values)
