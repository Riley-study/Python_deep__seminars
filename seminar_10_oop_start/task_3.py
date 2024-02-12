"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год,
full_name для вывода полного ФИО и т.п. на ваш выбор. Убедитесь,
что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
"""


class DataPerson:

    def __init__(self, name: str, sername: str, age: int):
        self.name = name
        self.sername = sername
        self.__age = age


    def birthday(self):
        self.__age += 1


    def __str__(self):
        return f"{self.name}  {self.sername}  {self.__age}"

if __name__ == '__main__':

    human_1 = DataPerson('Petr', 'Petrov', 27)
    human_2 = DataPerson('Sergey', 'Serov', 30)

    print(human_1)
    print(human_2)
