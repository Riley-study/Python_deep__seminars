# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл. Пользователи
# группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени. Убедитесь,
# что все идентификаторы уникальны независимо от уровня доступа. При перезапуске функции уже
# записанные в файл данные должны сохраняться.

import json
import os


def load_or_create(file_name: str):
    if file_name in os.listdir():
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    else:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump({}, f)
        return {}


def enter_user(level: str, id: str, name: str, file_name: str) -> None:
    data = load_or_create(file_name)
    for value in data.values():
        if id in value:
            raise ValueError("id already exist")
    data.setdefault(level, {})
    data[level].setdefault(id, name)
    data[level][id] = name
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    enter_user('5', '12345656', 'Alena4', 'data_task2.json')
