'''
    Para poder extraer alguna estadística, en una agencia de quiniela, se requiere saber cuál fue
    el mayor valor registrado en los sorteos comprendidos en un periodo de tiempo
    determinado, Terminar el proceso de carga de los números, cuando el valor leído sea
    mayor que novecientos noventa y nueve
'''
import random

mayor = 0

while True:
    num = random.randint(0, 1200)
    print(num)
    if num > 999:
        break
    
    if num > mayor:
        mayor = num

print(f'El número mayor fue: {mayor}')