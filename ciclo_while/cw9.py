'''
    Para elaborar la misma estadística, se necesita verificar que todos los valores ingresados sean
    mayor ó igual que cero; En caso contrario indicar que se trata de un error; ignorar el dato
    leído y leer el próximo.
'''
import random

mayor = 0

while True:
    num = random.randint(-100, 1200)
    if num > 999:
        print(num)
        break
    elif num > mayor:
        print(num)
        mayor = num
    elif num <= 0:
        print('Se ingreso un 0 o un valor menor')


print(f'El número mayor fue: {mayor}')