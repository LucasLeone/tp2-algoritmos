'''
    Se quiere calcular la raíz cuadrada y cuadrados respectivamente a una serie de quinientos
    pares ordenados. Interrumpir el proceso cuando la raíz del primer elemento sea igual al
    cuadrado del segundo elemento. En aquellos pares cuyo primer elemento sea menor que
    cero ignorar el par y leer el próximo.
'''
import math

i = 0

while True:
    i += 1

    if i > 500:
        break

    print('---- Nuevo par ordenado ----')
    x = int(input('Ingrese el primer valor: '))
    y = int(input('Ingrese el segundo valor: '))
    print(f'({x}, {y})')

    if x == 0:
        continue
    else:
        raizx = math.sqrt(x)
        raizy = math.sqrt(y)
        print(f'Raiz del primer valor: {raizx}')
        print(f'Raiz del segundo valor: {raizy}')

        cuadradox = x**2
        cuadradoy = y**2
        print(f'Cuadrado del primer valor: {cuadradox}')
        print(f'Cuadrado del primer valor: {cuadradoy}')

        if raizx == cuadradoy:
            print('La raiz del primer valor es igual al cuadrado del segundo valor.')
            break



