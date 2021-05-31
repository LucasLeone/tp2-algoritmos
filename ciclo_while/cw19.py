'''
    Ingresar de a uno una serie de números. Encontrar e Imprimir el mayor de todos los números
    pares, el proceso terminará cuando el número leído sea igual a cero.
'''

i = 0
mayor = 0

while True:
    num = int(input('Ingrese un numero: '))
    if num == 0:
        break

    if i == 0:
        mayor = num
        i = i + 1

    if num % 2 == 0:
        if num >= mayor:
            mayor = num

print(f'El numero mayor de todos los pares fue: {mayor}')