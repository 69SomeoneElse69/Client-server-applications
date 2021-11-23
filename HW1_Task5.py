"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице."""

import subprocess
import chardet
import platform

URL_1 = 'yandex.ru'
URL_2 = 'youtube.com'

URLS_LIST = [URL_1, URL_2]
RETRYS = '-n' if platform.system() == 'Windows' else '-c'

for url in URLS_LIST:
    args = ['ping', RETRYS, '4', url]
    YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
