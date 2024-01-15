# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

import decimal
from math import pi

diameter = float(input("Введите диаметр окружности: "))
radius = decimal.Decimal(diameter/2)   # привели к типу decimal
PI = decimal.Decimal(pi)

circle_sqare =PI*(radius**2)
circle_length = 2*PI*radius

print(f'Площадь круга = {circle_sqare} \n'  
      f'Длина окружности = {circle_length}')
