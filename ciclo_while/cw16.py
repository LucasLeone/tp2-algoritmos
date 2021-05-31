'''
    Leer por teclado una serie de valores, imprimiendo para cada valor su raíz cuadrada si es par
    y su cuadrado si es impar. Ultimo valor, cero (no debe ser procesado).
'''
import math

while True:
    num = int(input('Ingrese un numero: '))
    if num == 0:
        break

    if num % 2 == 0:
        print(f'La raiz cuadrada de {num} es: {math.sqrt(num)}')
    else:
        print(f'El cuadrado de {num} es: {num**2}')