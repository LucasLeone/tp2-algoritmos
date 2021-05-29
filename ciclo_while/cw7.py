'''
    En una serie de treinta y cuatro elementos, 
    se quiere calcular e imprimir el cuadrado de cada
    número, deberán ser leído dos uno por vez.
'''
import random

i = 0

while i < 34:
    i = i + 2
    num = random.randint(0, 50)
    num2 = random.randint(0, 50)
    print(f'Los cuadrados de {num} y {num2} son: {num**2} y {num2**2}')