'''
    Se quiere calcular e imprimir el cuadrado de cada número de una serie 
    de treinta elementos, los que se leen de a uno por vez.
'''

for i in range(0, 30):
    print('---- Nuevo numero ----')
    num = int(input('Ingrese un numero: '))

    print(f'El cuadrado de {num} es: {num**2}')