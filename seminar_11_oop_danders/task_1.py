# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора
# строки и время создания (time.time)
import time


class MyString(str):
    def __new__(cls, value: str, name: str = None):
        instance = super().__new__(cls, value)  # вызвали родительский метод new и передали туда значение value
        instance.name = name  # добавляем нужные поля, которых нет у родительского класса
        instance.time = time.ctime()
        return instance # это и будет self с которым будет работать __init__


if __name__ == '__main__':
    t = MyString("HELLO? i'm one string", 'Alex')
    t2 = MyString("HELLO? i'm two string", 'Jo')
    t3 = MyString("HELLO? i'm three string")
    st = t + t2 + t3 + ' Hero'
    print(type(st))
    print(f'{t = }\t{t.name = }\t{t.time}')
    print(f'{t2 = }\t{t2.name = }\t{t2.time}')
    print(f'{t3 = }\t{t3.name = }\t{t3.time}')