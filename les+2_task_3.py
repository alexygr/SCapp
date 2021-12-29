"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

my_dict = {
    'list': [1, 2, 3, 4, 5],
    'integer': 1000,
    'inner_dict': {'1': '1000€', '2': '2000€', '3': '3000€', '4': '4000€'},
}


def write_data_to_yaml(data):
    with open('file.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_style=False, allow_unicode=True, sort_keys=False, indent=4)


def read_data_from_yaml():
    with open('file.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


write_data_to_yaml(my_dict)


if my_dict == read_data_from_yaml():
    print('Данные  совпадают с данными файла')
else:
    print('Данные не совпадают с данными файла')
