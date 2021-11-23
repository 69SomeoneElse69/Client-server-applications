"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode)."""

WORD_1 = 'разработка'
WORD_2 = 'администрирование'
WORD_3 = 'protocol'
WORD_4 = 'standard'

WORDS_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]

for item in WORDS_LIST:
    ENC_STR_BYTES = item.encode('utf-8')
    DEC_STR = ENC_STR_BYTES.decode('utf-8')
    print(f'кодирование в utf-8: {ENC_STR_BYTES}, \nполучен тип: {type(ENC_STR_BYTES)}')
    print(f'декодирование: {DEC_STR}, \nполучен тип: {type(DEC_STR)}')
    print("*" * 30)
