'''
    Leer cien pares ordenados (X,V) de números, y de cada par,
    imprimir el cociente (cociente X/Y).
'''
import random

i = 0
x = 0
y = 0

while i < 100:
    i = i + 1
    num_x = random.randint(0, 100)
    num_y = random.randint(0, 100)
    x = x + num_x
    y = y + num_y
    print(f'El par ordenado es: {num_x}, {num_y}')
    print(f'Y el cociente es: {num_x / num_y}')
