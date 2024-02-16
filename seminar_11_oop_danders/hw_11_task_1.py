# Разработайте программное обеспечение для ведения журнала событий. Вам необходимо создать класс,
# который будет представлять строки журнала и включать в себя информацию об авторе и времени создания каждой записи.

import datetime


class MyStr(str):
    def __new__(cls, value: str, author: str = None):
        instance = super().__new__(cls, value)  # вызвали родительский метод new и передали туда значение value
        instance.author = author  # добавляем нужные поля, которых нет у родительского класса
        instance.time = datetime.datetime.now()

        return instance  # это и будет self с которым будет работать __init__

    def __init__(self, value, author):
        self.value = value
        self.author = author
        self.time = datetime.datetime.now()

    def __str__(self):
        formatted_time = self.time.strftime('%Y-%m-%d %H:%M')
        return f'{self.value} (Автор: {self.author}, Время создания: {formatted_time})'

    def __repr__(self):
        return f"'{self.value}', '{self.author}'"


if __name__ == '__main__':
    event = MyStr("Завершилось тестирование", "John")
    print(event)
    my_string = MyStr("Пример текста", "Иван")
    print(my_string)
    my_string = MyStr("Мама мыла раму", "Маршак")
    print(repr(my_string))
