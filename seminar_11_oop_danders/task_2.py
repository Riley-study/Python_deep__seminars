# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
# в пару списков-архивов, которые также являются свойствами экземпляра.
# Доработаем класс Архив из задачи 2. Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    _instance = None

    def __new__(cls, text, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # передали функцию от родительского класса (object)
            cls._instance.old_text = []  # инициализировали свойство, изначально пустой список
            cls._instance.old_name = []
        else:
            cls._instance.old_text.append(cls._instance.text)
            cls._instance.old_name.append(cls._instance.name)

        return cls._instance

    def __init__(self, text: str, name: str):
        self.text = text
        self.name = name

    def __str__(self):
        return f'a= {a.name}, text = {a.text}'

    def __repr__(self):
        return f'Archive (data= {self.text=},name= {self.name})'


if __name__ == '__main__':
    a = Archive('123', "name1")
    print(a)
    # print(f'a= {a.name}, text = {a.text}')
    # print(f'{a.old_text}')
    # print(f'{a.old_name}')
    b = Archive('345', 'name2')
    print(b.__repr__())
    # print(f'b= {b.name}, text = {b.text}')
    # print(f'{a.old_text}')
    # print(f'{a.old_name}')
    # c = Archive("text!!", 'name3')
    # print(f'c= {c.name}, text = {c.text}')
    # print(f'{b.old_text}')
    # print(f'{b.old_name}')
