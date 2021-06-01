'''
    Leer una serie de números enteros cuyo último debe ser de valor negativo 
    y no debe ser procesado, e indicar cuántos de estos números son pares.
'''

pares = 0
i = 0

while i < 5:
    i = i + 1

    num = int(input('Ingrese un numero: '))
    if i == 5:
        break

    if num % 2 == 0:
        pares = pares + 1

print(f'Hay un total de {pares} numeros pares')