# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
# в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет,
# вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# Добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

from task_4 import User, load_users
from task_3 import LevelError, AccessError, ProjectException


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



if __name__ == '__main__':
    pr1 = Project('task04.json')
    pr1.authorization("12345656", "Alex")
    pr1.add_user('776767787', 'Nata', '8')
    print(pr1.data)
