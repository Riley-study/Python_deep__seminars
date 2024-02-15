"""
Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса
Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию
 глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

    Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка,
Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 100:
            return "Гигант"
        return "Обычный"


class AnimalFactory:
    @staticmethod
    def create_animal(type_animal, *args):
        if type_animal == "Bird":
            new_animal = Bird(args[0],args[1])
        elif type_animal == "Fish":
            new_animal = Fish(args[0],args[1])
        elif type_animal == "Mammal":
            new_animal = Mammal(args[0],args[1])
        else:
            raise ValueError("Недопустимый тип животного")
        return new_animal



if __name__ == '__main__':
    # b = Bird('bird1', 4)
    # f = Fish('fish1', 150.0)
    # m = Mammal('mammal1', 150)
    #
    # print(f"{b.wing_length()=}")
    # print(f"{f.depth()=}")
    # print(f"{m.category()=}")

    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

    # Вывод результатов
    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())

