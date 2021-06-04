'''
    Se dispone de veinte pares ordenados de números; 
    se debe leer e imprimir la diferencia de cada par.
'''


for i in range(0, 20):
    print('---- Nuevo par ordenado ----')
    x = int(input('Ingrese el primer valor: '))
    y = int(input('Ingrese el segundo valor: '))

    diferencia = x - y

    print(f'La diferencia es: {diferencia}')