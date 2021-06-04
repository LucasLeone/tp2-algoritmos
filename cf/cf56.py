'''
    Se dispone de una lista con doscientos pares ordenados (X, Y}, que deberán ser lerdos uno
    por uno, se quiere imprimir los dos posibles cocientes de cada par.
'''

for i in range(0, 200):
    x = int(input('Ingrese el primer valor: '))
    y = int(input('Ingrese el segundo valor: '))

    print(f'Los 2 posibles cocientes entre {x} y {y} son: {x / y} y {y / x}')