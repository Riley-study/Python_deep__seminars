# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответствует формату.

from datetime import datetime, date
from task_3_logging import log_decorator

MONTH = {
    "января": 1, "февраля": 2, "марта": 3,
    "апреля": 4, "мая": 5, "июня": 6,
    "июля": 7, "августа": 8, "сентября": 9,
    "октября": 10, "ноября": 11, "декабря": 12
}
WEEKDAYS = {
    "понедельник": 1,
    "вторник": 2,
    "среда": 3,
    "четверг": 4,
    "пятница": 5,
    "суббота": 6,
    "воскресенье": 7
}

@log_decorator
def string_to_date(s: str) -> datetime:
    week, weekday, month = s.split()
    week = week[0]
    y = datetime.now().year
    month_num = MONTH[month]
    # print(month_num)
    first_day = date(day=1, month=month_num, year=y)
    weekday_first_day = first_day.weekday() + 1
    if weekday_first_day > WEEKDAYS[weekday]:
        day_by_date = 7 * (int(week)) + (weekday_first_day - WEEKDAYS[weekday]) - 1
    else:
        day_by_date = 7 * (int(week) - 1) + (- weekday_first_day + WEEKDAYS[weekday]) + 1
    found_date = date(day=day_by_date, month=month_num, year=y)
    print(f'{s} - {found_date}')
    return found_date


if __name__ == '__main__':
    string_to_date('1-й четверг ноября')  # 7 ноября
    string_to_date('1-й четверг февраля')  # 1 февраля
    string_to_date('2-я среда мая')  # 8 мая
    string_to_date('3-я вторник апреля')  # 16 апреля
    string_to_date('4-й вторник апреля')  # 23 апреля
    string_to_date('5-й четверг февраля')  # 23 апреля
