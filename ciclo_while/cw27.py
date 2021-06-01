'''
    Para una serie de doscientos valores, calcular las raíces 
    cuadradas de lados los elementos positivos.
'''
import random
import math

i = 0

while i < 200:
    i = i + 1
    num = random.randint(-200, 200)

    if num > 0:
        print(f'La raiz cuadrada de {num} es: {math.sqrt(num)}')