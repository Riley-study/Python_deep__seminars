"""
Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть шестизначный идентификационный номер и уровень доступа
(остаток от суммы цифр id делённой на семь)
"""
from task_3 import DataPerson


class Employee(DataPerson):

    def __init__(self, emp_id: int, *args, **kwargs):
        if len(str(emp_id)) != 6:
            raise ValueError("Некорректный идентификационный номер")
        self.emp_id = emp_id
        self.emp_level = sum(map(int, str(emp_id))) % 7
        super().__init__(*args, **kwargs)


# p1 = DataPerson()
e = Employee(176767, "Ivan", "Petrov", 33)
e2 = Employee(188989, "Ivan", "Ogonkov", 33)
print(f"{e.emp_id=}, {e.emp_level=}, {e.name}, {e.sername}")
print(e2)
