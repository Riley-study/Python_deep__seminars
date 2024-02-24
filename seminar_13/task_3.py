# Создайте класс с базовым исключением и дочерние классы-исключения: ошибка уровня, ошибка доступа.
class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __str__(self):
        return f'Уровень пользователя ниже, чем ваш уровень'


class AccessError(ProjectException):
    def __str__(self):
        return f'Такого пользователя не существует.'

