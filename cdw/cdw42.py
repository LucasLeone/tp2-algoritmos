'''
    Leer de a uno una serie de números e imprimir un ••• al lado de cada número par. El proceso
    termina cuando la suma de los números leídos sea mayor o igual a mil.
'''

suma = 0

while True:
    if suma >= 1000:
        break

    num = int(input('Ingrese un numero: '))
    suma += num

    if num % 2 == 0:
        print(f'{num}•••')