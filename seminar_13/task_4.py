# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра. Отдельно напишите функцию,
# которая считывает информацию из JSON файла и формирует множество пользователей.

import json
import os


class User:
    def __init__(self, id_, level, name):
        self.id, self.level, self.name = id_, level, name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash(self.id + self.name)

    def __repr__(self):
        return f'User({self.id}, {self.level}, {self.name})'


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


def load_users(file_name: str) -> set[User]:
    data = load_or_create(file_name)
    res = set()
    for level, inner_dict in data.items():
        for id_, name in inner_dict.items():
            res.add(User(id_, level, name))
    return res


if __name__ == '__main__':
    enter_user('5', '12345656', 'Alex', 'task04.json')
    enter_user('7', '12345657', 'Ben', 'task04.json')
    print(load_users('task04.json'))
