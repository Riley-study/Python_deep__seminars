import json
import os

class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __str__(self):
        return f'Уровень пользователя ниже, чем ваш уровень'


class AccessError(ProjectException):
    def __str__(self):
        return f'Такого пользователя не существует.'

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


class Project:
    def __init__(self, file_name):
        self.data = load_users(file_name)
        self.admin = None

    def authorization(self, id_, name):
        temp_user = User(id_, '', name)
        if temp_user not in self.data:
            raise AccessError
        for user in self.data:
            if user == temp_user:
                self.admin = user  # сравнили всех пользователей в базе с авторизовавшимся, назначили его админом

    def add_user(self, id_, name, level):
        if not self.admin:
            raise ProjectException
        if int(level) < int(self.admin.level):
            raise LevelError
        self.data.add(User(id_, level, name))