import chardet   # необходима предварительная инсталляция!
import subprocess
import platform
import locale


_1 = """
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
"""


def task_1(text):
    return type(text), text


print(_1)
print(*task_1('разработка'))
print(*task_1('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'))
print(*task_1('сокет'))
print(*task_1('\u0441\u043e\u043a\u0435\u0442'))
print(*task_1('декоратор'))
print(*task_1('\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'))

_2 = """
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это небходимо в автоматическом,
а не ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""


def task_2(text):
    text = eval(f'b\'{text}\'')
    return type(text), text, len(text)


print(_2)
words = 'class', 'function', 'method'
for word in words:
    print(*task_2(word))

_3 = """
3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе. Для проверки
 правильности работы кода используйте значения: «attribute», «класс», «функция», «type»
"""


def task_3(text):
    try:
        text = eval(f'b\'{text}\'')
    except SyntaxError as err:
        return False
    else:
        return True


print(_3)
words1 = 'attribute', 'класс', 'функция', 'type'

for word in words1:
    if task_3(word):
        print(f'Word "{word}" possible convert to bytes type')
    else:
        print(f'Word "{word}" impossible convert to bytes type')


_4 = """
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления 
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""


def task_4(text):
    if isinstance(text, bytes):
        return bytes.decode(text, encoding='utf-8')
    else:
        return str.encode(text, encoding='utf-8')


print(_4)
words2 = 'разработка', 'администрирование', 'protocol', 'standard'
words2 = list(map(task_4, words2))
print(*words2, sep='\n')
words2 = list(map(task_4, words2))
print(*words2, sep='\n')


_5 = """
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
 (предварительно определив кодировку выводимых сообщений).
"""


def ping(address):
    default_encoding = locale.getpreferredencoding()
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', address]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode(default_encoding)
        print(line.decode(default_encoding))


print(_5)
ping('yandex.ru')
ping('youtube.com')


_6 = """
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!).
Затем открыть этот файл и вывести его содержимое на печать. ВАЖНО: файл должен быть открыт без ошибок вне 
зависимости от того, в какой кодировке он был создан!
"""

print(_6)
text = 'сетевое программирование', 'сокет', 'декоратор'
f = open('test.txt', 'w', encoding='utf-8')
for el in text:
    f.write(f'{el}\n')
f.close()
print(f)

with open('test.txt', 'rb') as f:
    content = f.read()
encoding = chardet.detect(content)['encoding']
print('encoding: ', encoding)


# --- 3. Теперь открываем файл в УЖЕ известной нам кодировке
with open('test.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()
