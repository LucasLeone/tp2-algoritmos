'''
    Se dispone de una serie de doscientos cincuenta números menores que cien y mayores que
    cero, se quiere saber cuántos de estos son primos
'''
import random

i = 0
primos = 0

while i < 250:
    i = i + 1

    num = random.randint(0, 100)

    for divisor in range(2, num):
        if num % divisor == 0:
            pass
        else:
            primos = primos + 1
            break

print(f'Hay un total de {primos} numeros primos')