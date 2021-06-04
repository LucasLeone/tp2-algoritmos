'''
    Se dispone de cien pares ordenados de números y 
    se quiere imprimir el cociente de cada uno.
'''

for i in range(0, 100):
    print('---- Nuevo par ordenado ----')
    x = int(input('Ingrese el primer valor: '))
    y = int(input('Ingrese el segundo valor: '))

    print(f'El cociente entre estos 2 numeros es: {x / y}')