'''
    Leer cincuenta números e indicar la cantidad de valores mayores que diez.
'''

mayores = 0

for i in range(0, 50):
    num = int(input('Ingrese un numero: '))
    if num > 10:
        mayores += 1

print(f'Hay un total de {mayores} numeros mayores a 10')