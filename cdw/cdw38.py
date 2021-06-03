'''
    Leer un número, calcular la raíz cúbica y así sucesivamente hasta que el resultado sea menor
    que uno imprimir los resultados parciales y finales. Controlar que el número leído sea
    mayor que cero.
'''
import math

num = int(input('Ingrese un numero: '))
if num < 0:
    quit()

while num > 1:
    raizc = math.sqrt(num)
    print(f'Resultado parcial: {raizc}')
    num = raizc

    if num < 1:
        print(f'El numero final es: {num}')
        break