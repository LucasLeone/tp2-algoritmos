'''
    Leer una serie de pares ordenados, encontrar e imprimir el par cuya suma sea mayor, además
    ignorar todos aquellos pares en que algún elemento sea menor que diez o mayor que
    noventa y nueve. La cantidad de pares leídos es de mil.
'''

mayorx = 0
mayory = 0
mayor_suma = 0

i = 0

while True:
    i += 1
    
    if i > 1000:
        break

    print('---- Nuevo par ordenado ----')
    valorx = int(input('Ingrese el primer valor: '))
    valory = int(input('Ingrese el segundo valor: '))

    total = valorx + valory

    if i == 1:
        mayor_suma = total

    if total > mayor_suma:
        mayorx = valorx
        mayory = valory
        mayor_suma = total

print(f'La mayor suma son a partir del par ordenado ({mayorx}, {mayory}) que da como total: {mayor_suma}')