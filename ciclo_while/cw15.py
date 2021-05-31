'''
    Leer de a uno, una serie de números enteros, e imprimir un “*” al lado de cada número par.
    El proceso termina cuando el número leído sea cero.
'''

while True:
    num = int(input('Ingrese un numero: '))
    if num == 0:
        break

    if num % 2 == 0:
        print(f'{num}*')