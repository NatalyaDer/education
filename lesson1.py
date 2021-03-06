# Задание 1

development = 'разработка'
print(type(development))
print(development)
development_simbol = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(development_simbol)

socket = 'сокет'
print(type(socket))
print(socket)
socket_simbol = '\u0441\u043e\u043a\u0435\u0442'
print(socket_simbol)

decorator = 'декоратор'
print(type(decorator))
print(decorator)
decorator_simbol = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(decorator_simbol)

# Задание 2

var_1 = 'class'
var_2 = 'function'
var_3 = 'method'

words = [var_1, var_2, var_3]

for el_str in words:
    el = eval(b'el_str')
    print(type(el))
    print(el)
    print(len(el))

# Задание 3

var_1 = 'attribute'
var_2 = 'класс'
var_3 = 'функция'
var_4 = 'type'

var_list = [var_1, var_2, var_3, var_4]

for word in var_list:
    try:
        word.encode('ascii')
    except UnicodeEncodeError:
        print(f' Слово "{word}" невозможно записать в виде байтовой строки')

# Задание 4

development_1 = 'разработка'
development_1_str = str.encode(development_1, encoding='utf-8')
print(development_1_str)

administration = 'администрирование'
administration_str = str.encode(administration, encoding='utf-8')
print(administration_str)

protocol = 'protocol'
protocol_str = str.encode(protocol, encoding='utf-8')
print(protocol_str)

standard = 'standard'
standard_str = str.encode(standard, encoding='utf-8')
print(standard_str)

development_b = b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
development_dec = bytes.decode(development_b, encoding='utf-8')
print(development_dec)

administration_b = b'\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435'
administration_dec = bytes.decode(administration_b, encoding='utf-8')
print(administration_dec)

protocol_b = b'\u0070\u0072\u006f\u0074\u006f\u0063\u006f\u006c'
protocol_dec = bytes.decode(protocol_b, encoding='utf-8')
print(protocol_dec)

standard_b = b'\u0073\u0074\u0061\u006e\u0064\u0061\u0072\u0064'
standard_dec = bytes.decode(standard_b, encoding='utf-8')
print(standard_dec)

# Задание 5

import chardet
import subprocess
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
result = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in result.stdout:
    results = chardet.detect(line)
    print(result)
    line = line.decode(results['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

param_you = '-n' if platform.system().lower() == 'windows' else '-c'
args_1 = ['ping', param_you, '2', 'youtube.com']
result_param_you = subprocess.Popen(args_1, stdout=subprocess.PIPE)
for line in result_param_you.stdout:
    result_1 = chardet.detect(line)
    print(result_param_you)
    line = line.decode(result_1['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

# Задание 6

from chardet import detect
f = open('test_file.txt', 'w', encoding='utf-8')
f.write('сетевое программирование, сокет, декоратор')
f.close()

with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding :', encoding)

with open('test_file.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')


