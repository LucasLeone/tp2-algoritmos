'''
    Leer una serie de números enteros. que contenga como máximo veinte elementos, en caso de
    ingresar un valor negativo o la cantidad de números ingresados supere los veinte, detener
    el proceso e informar mediante un mensaje cuántos son mayores que 100.
'''
import random

i = 0
mayores = 0

while i < 20:
    i = i + 1
    num = random.randint(-100, 200)
    print(num)
    if num > 100:
        mayores = mayores + 1
    elif num < 0:
        break

print(f'Hay un total de {mayores} números mayores a 100')