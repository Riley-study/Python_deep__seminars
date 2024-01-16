import fractions

# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.


frac1 = "1/2"
frac2 = "1/3"
numerator_1 = int(frac1[0])
denominator_1 = int(frac1[2])
numerator_2 = int(frac2[0])
denominator_2 = int(frac2[2])

res_summ_fractions = fractions.Fraction(numerator_1, denominator_1) + fractions.Fraction(numerator_2, denominator_2)
res_mult_fractions = fractions.Fraction(numerator_1, denominator_1) * fractions.Fraction(numerator_2, denominator_2)

res_summ = str(numerator_1 * denominator_2 + numerator_2 * denominator_1) + "/" + str(denominator_1 * denominator_2)
res_mult = str(numerator_1 * numerator_2) + "/" + str(denominator_1 * denominator_2)

print(f'Сумма дробей: {res_summ} \n'
      f'Произведение дробей: {res_mult}')
print(f'Сумма дробей: {res_summ_fractions} \n'
      f'Произведение дробей: {res_mult_fractions}')
