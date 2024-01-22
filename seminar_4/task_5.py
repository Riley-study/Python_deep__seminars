# Функция принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def awards_count(names: list[str], salaries: list[int], bonuses: list[str]) -> dict[str, float]:
    res = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        res[name] = round(salary * float(bonus.replace("%", "")) / 100, 2)
    return res

list_names = ['Alex', 'Yuriy', 'Olga']
list_salaries = [90_000, 85_000, 110_000]
list_bonus = ['10.2%', '5%', '10%']

print(awards_count(list_names, list_salaries, list_bonus))