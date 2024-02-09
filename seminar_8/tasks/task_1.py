# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json


def txt_to_json(source, output):
    with open(source, 'r', encoding='utf-8') as f:
        data = f.read()

    data_dict = {}
    for line in data.split('\n'):
        name, number = line.split(' ')
        data_dict[name.capitalize()] = float(number)

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4)


if __name__ == '__main__':
    txt_to_json('file_1.txt', "file_2.json")
