import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)
global bank_account
bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):  # Проверка кратности суммы при пополнении и снятии.
    if amount % 50 != 0:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False
    return True


def deposit(amount):  # Пополнение счёта.
    global bank_account
    if check_multiplicity(amount):
        bank_account += decimal.Decimal(amount)
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')


def withdraw(amount):  # Снятие денег.
    global bank_account
    sum_to_remove = round(min(max(amount * PERCENT_REMOVAL, MIN_REMOVAL), MAX_REMOVAL),0)
    if (amount + sum_to_remove) <= bank_account:
        if check_multiplicity(amount):
            bank_account -= (amount + sum_to_remove)
            operations.append(f'Снятие с карты {amount} у.е. '
                          f'Процент за снятие {sum_to_remove} у.е.. Итого {bank_account} у.е.')
    else:
        check_multiplicity(amount)
        operations.append(f'Недостаточно средств. '
                          f'Сумма с комиссией {amount + sum_to_remove} у.е. На карте {bank_account} у.е.')


def exit():  # Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
    global bank_account
    if bank_account > RICHNESS_SUM:
        richness_tax = round(bank_account*RICHNESS_PERCENT, 4)
        bank_account -= richness_tax
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {richness_tax} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

# deposit(173)
# withdraw(21)
# exit()

# Сумма должна быть кратной 50 у.е.
# Сумма должна быть кратной 50 у.е.
# ['Недостаточно средств. Сумма с комиссией 51 у.е. На карте 0 у.е.', 'Возьмите карту на которой 0 у.е.']


# deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()
# ['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.', 'Снятие с карты 200 у.е.
# Процент за снятие 30 у.е.. Итого 999999999999770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е..
# Итого 999999999999440 у.е.', 'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.', 'Снятие с карты 3000 у.е.
# Процент за снятие 45.000 у.е.. Итого 999999999996895.000 у.е.', 'Вычтен налог на богатство 0.1% в сумме
# 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.', 'Возьмите карту на которой 899999999997205.5000 у.е.']


# deposit(1000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()

# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е..
# Итого 770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 440 у.е.', 'Пополнение карты на 500 у.е.
# Итого 940 у.е.', 'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.',
# 'Возьмите карту на которой 940 у.е.']

# deposit(1000)
# withdraw(200)
# exit()

# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
#  'Возьмите карту на которой 770 у.е.']

# deposit(10000)
# withdraw(4000)
# exit()

# ['Пополнение карты на 10000 у.е. Итого 10000 у.е.',
#  'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)

