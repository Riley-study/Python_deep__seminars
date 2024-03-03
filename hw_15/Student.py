import csv
import logging
from functools import wraps

FORMAT = '{levelname:<8} - {asctime}. Добавлено {msg}'
logging.basicConfig(format=FORMAT, filename='Students.log', encoding='utf-8', style='{', level=logging.NOTSET)

def log_decorator(func):
    logger = logging.getLogger(__name__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename=f'{func.__name__}.log', encoding='utf-8', level=logging.NOTSET)
        res = func(*args, **kwargs)
        logging.debug(f'{args.__str__()} {kwargs} {res}')
        return res

    return wrapper
class NameDescriptor:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.replace(' ', '').isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        if not value.istitle():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        return setattr(instance, self.param_name, value)


class Student:
    name = NameDescriptor()
    def load_subjects(self, file_name: str):
        list_of_subjects = []
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for subject in row:
                    list_of_subjects.append(subject)
        return list_of_subjects

    @log_decorator
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.list_of_subjects = self.load_subjects(subjects_file)
    @log_decorator
    def add_grade(self, subject, grade):
        if not 2 <= grade <= 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        if subject in self.list_of_subjects:
            if subject in self.subjects:
                self.subjects[subject]["grade"] = []
                self.subjects[subject]["grade"].append(grade)
            else:
                self.subjects[subject] = {"grade": [grade]}
        else:
            raise ValueError(f"Предмет {subject} не найден")

    @log_decorator
    def add_test_score(self, subject, test_score):
        if not 0 <= test_score <= 100:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        if subject in self.list_of_subjects:
            if subject in self.subjects:
                self.subjects[subject]["test"] = []
                self.subjects[subject]["test"].append(test_score)
            else:
                self.subjects[subject] = {"test": [test_score]}
        else:
            raise ValueError(f"Предмет {subject} не найден")


    @log_decorator
    def get_average_test_score(self, subject):
        if not subject in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        list_marks = self.subjects[subject]['test']
        return sum(list_marks) / len(list_marks)

    @log_decorator
    def get_average_grade(self):
        list_marks = []
        for subj, value in self.subjects.items():
            for exam, mark in value.items():
                if exam == 'grade':
                    list_marks.append(mark)
        return (sum(map(sum, list_marks))) / len(list_marks)

    def __str__(self):
        return f'Студент: {self.name} ' + ', '.join(self.subjects.keys())


# if __name__ == '__main__':
#     # csv_file = "subjects.csv"
#     student = Student("Иван Иванов", "subjects.csv")
#
#     student.add_grade("Математика", 4)
#     student.add_test_score("Математика", 85)
#
#     student.add_grade("История", 5)
#     student.add_test_score("История", 92)
#     print(student)
#     average_grade = student.get_average_grade()
#     print(f"Средний балл: {average_grade}")
#
#     average_test_score = student.get_average_test_score("Математика")
#     print(f"Средний результат по тестам по математике: {average_test_score}")

