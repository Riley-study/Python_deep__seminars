# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
MONTHS = {
    1: range(1, 32),
    2: range(1, 29),
    3: range(1, 32),
    4: range(1, 31),
    5: range(1, 32),
    6: range(1, 31),
    7: range(1, 32),
    8: range(1, 32),
    9: range(1, 31),
    10: range(1, 32),
    11: range(1, 31),
    12: range(1, 32)
}


def parse_data(date: str) -> bool:
    d, m, y = map(int, date.split('.'))
    return _year_is_valid(y) and _month_is_valid(m) and _day_is_valid(d, m, y)


def _day_is_valid(day, month, year) -> bool:
    if _is_leap_year(year) and month == 2:
        return day in range(1, 30)
    return day in MONTHS[month]


def _month_is_valid(month) -> bool:
    return month in range(1, 13)


def _year_is_valid(year) -> bool:
    return year in range(1, 10_000)


def _is_leap_year(year) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == '__main__':
    print(parse_data('28.02.2024'))
    print(parse_data('29.02.2023'))
    print(parse_data('31.04.2000'))
    print(parse_data('32.12.1988'))
