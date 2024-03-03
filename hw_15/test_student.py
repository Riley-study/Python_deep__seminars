# 1. Взять класс студент из дз 12-го семинара, добавить запуск из командной строки
# (передача в качестве аргумента название csv-файла с предметами), логирование и
# написать 3-5 тестов с использованием pytest.
import pytest
from Student import Student


@pytest.fixture
def st1():
    return Student("Katya Isaeva", "subjects.csv")


def test_init_student():
    assert Student("Katya Isaeva", "subjects.csv") is not None, "Error to create a student"


def test_load_subjects(st1):
    assert st1.load_subjects('subjects.csv') == ['Maths', 'History', 'Biology', 'Physics']

def test_add_wrong_grade(st1):
    with pytest.raises(ValueError):
        st1.add_grade('Maths', 6)

def test_add_wrong_test_score(st1):
    with pytest.raises(ValueError):
        st1.add_test_score('Maths', 150)

def test_get_average_test_score(st1):
    st1.add_test_score('Maths', 100)
    assert st1.get_average_test_score('Maths') == 100


if __name__ == '__main__':
    pytest.main(['-v'])
