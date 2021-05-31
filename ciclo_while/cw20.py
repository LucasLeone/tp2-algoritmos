'''
    Ingresar de a uno, una serie de números. Encontrar e imprimir el mayor de todos los números
    pares cuyo número de orden sea par, el proceso terminará cuando el número lerdo sea
    igual a cero.
'''

i = 0
mayor = 0

while True:
    num = int(input('Ingrese un numero: '))
    if num == 0:
        break

    if i == 0 and num % 2 == 0:
        mayor = num
        i = i + 1

    if num > mayor and num % 2 == 0:
        mayor = num

print(f'El numero mayor de los pares fue: {mayor}')