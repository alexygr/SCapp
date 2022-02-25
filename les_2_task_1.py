"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
 info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import re
import chardet
import csv

FILES = ('info_1.txt', 'info_2.txt', 'info_3.txt')


def get_data(args):
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы'], ['Название ОС'], ['Код продукта'], ['Тип системы']]

    for each in args:
        with open(each, 'rb') as file:
            content = file.read()
        encoding = chardet.detect(content)
        content = str(content, encoding['encoding'])

        os_prod_list.append(re.search(r'Изготовитель системы:\s+(\w+)', content).group(1))
        os_name_list.append(re.search(r'Название ОС:\s+([^\r]+)', content).group(1))
        os_code_list.append(re.search(r'Код продукта:\s+(\S+)', content).group(1))
        os_type_list.append(re.search(r'Тип системы:\s+([^\r]+)', content).group(1))

    main_data[0].extend(os_prod_list)
    main_data[1].extend(os_name_list)
    main_data[2].extend(os_code_list)
    main_data[3].extend(os_type_list)

    return main_data


def write_to_csv(file_name):
    data = get_data(FILES)
    with open(file_name, 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for i in range(len(data)):
            row = []
            for j in range(len(data[i])):
                row.append(data[j][i])
            csv_writer.writerow(row)


if __name__ == '__main__':
    write_to_csv('result.csv')
