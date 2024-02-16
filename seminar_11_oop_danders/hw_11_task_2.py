# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании экземпляра класса Archive с указанием текстовой и числовой записи (text и number),
# записи добавляются в соответствующие атрибуты archive_text и archive_number. Если архив уже существует,
# текущие записи (text и number) добавляются в архив.
# Метод __str__ возвращает строковое представление объекта, включая текущие записи (text и number)
# и архивированные записи (archive_text и archive_number).
# Метод __repr__возвращает строковое представление объекта, которое можно использовать для создания
# нового объекта того же класса с теми же записями.

class Archive:
    _instance = None

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # передали функцию от родительского класса (object)
            cls._instance.archive_text = []  # инициализировали свойство, изначально пустой список
            cls._instance.archive_number = []
        return cls._instance

    def __init__(self, text: str, number: float):
        self.text = text
        self.number = number
        self.archive_text.append(self.text)
        self.archive_number.append(self.number)

    def __str__(self):
        return f'Text is {self.text}, and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    # Text is Запись 2 and number is 3.14. Also['Запись 1', 'Запись 2'] and [42, 3.14]

    def __repr__(self):
        return f'Archive (text= {self.text}, number= {self.number})'


if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    print(archive1)
    print(archive1.__repr__())
    archive2 = Archive("Запись 2", 3.14)
    print(archive2)
    print(archive2.__repr__())
    archive3 = Archive("Запись 3", 444)
    print(archive3)
    print(archive3.__repr__())
