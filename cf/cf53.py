'''
    Se debe calcular e imprimir el producto de todas las X y de todas las Y 
    de sesenta y tres pares ordenados de números enteros.
'''

for i in range(0, 63):
    print('---- Nuevo par ordenado ----')
    x = int(input('Ingrese el primer numero entero: '))
    y = int(input('Ingrese el segundo numero entero: '))

    print(f'El producto de este par ordenado es: {x * y}')