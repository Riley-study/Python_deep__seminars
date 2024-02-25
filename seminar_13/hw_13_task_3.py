class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    #     self._age += 1
# def birthday(self):
    def __init__(self, first_name, second_name, surname, age):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname
        self._age = age
        if self.first_name == "":
            raise InvalidNameError(f'Invalid name: {self.first_name}. Name should be a non-empty string.')
        if not int(self._age) > 0:
            raise InvalidAgeError(f'Invalid age: {self._age}. Age should be a positive integer.')
    def get_age(self):
        return self._age


# def full_name(self):
#     print(f"name: {self.name}\nsername: {self.sername}\nage: {self.__age}")


class Employee(Person):
    def __init__(self, first_name, second_name, surname, age, id_num):
        super().__init__(first_name, second_name, surname, age)
        self.id_num = id_num
        self.level = sum(map(int, str(id_num))) % 7
        if len(str(self.id_num)) != 6:
            raise InvalidIdError(
                f'Invalid id: {self.id_num}. Id should be a 6-digit positive integer between 100000 and 999999.')


if __name__ == '__main__':
    # person = Person("", "John", "Doe", 30)
    # empl = Employee('444555', "", "", "Doe", 30)
    # print(person)
    employee = Employee("Bob", "Johnson", "Brown", 40, 123456)
    # person = Person("Alice", "Smith", "Johnson", 25)
    # print(person.get_age())
