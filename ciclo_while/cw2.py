'''
    Leer una serie de cincuenta números enteros.
    Informar cuantos son mayores que 100.
'''
import random

i = 0
mayores = 0

while i < 50:
    i = i + 1
    num = random.randint(0, 200)
    print(num)
    if num > 100:
        mayores = mayores + 1

print(f'Hay un total de {mayores} números mayores')