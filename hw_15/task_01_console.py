# 1. Взять класс студент из дз 12-го семинара, добавить запуск из командной строки
# c передачей в качестве аргумента название csv-файла с предметами
# (добавлен еще аргумент student_name, чтобы была возможность возвращать готовый экземпляр класса)

from Student import Student, log_decorator
import argparse

@log_decorator
def st_parser():
    parser = argparse.ArgumentParser(description="Student performance in subjects")
    parser.add_argument('-stn', '--student_name')
    parser.add_argument('-fn', '--file_name', default='subjects.csv')
    args = parser.parse_args()
    student_to_analise = Student(args.student_name, args.file_name)

    return student_to_analise


if __name__ == '__main__':

    student = st_parser()

    student.add_grade("Maths", 4)
    student.add_test_score("Maths", 85)

    student.add_grade("History", 5)
    student.add_test_score("History", 92)
    print(student)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Maths")
    print(f"Средний результат по тестам по математике: {average_test_score}")

#  python .\task_01_console.py -stn 'Ivan Petrov'