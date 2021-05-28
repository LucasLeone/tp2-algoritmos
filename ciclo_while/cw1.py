'''
    Leer una serie de cincuenta números enteros.
'''
import random

i = 0

while i < 50:
    i = i + 1
    num = random.randint(0, 100)
    print(num)