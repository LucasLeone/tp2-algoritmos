'''
    En una lista de artículos compuesta por 'los siguientes datos: COD: Código. CAN:
    Cantidad, IMP: Importe. FEC: Fecha. DESC: Descripción. Calcular el promedio de todos los
    Importes cuyo código sea impar (fin de proceso COD=O).
    Modificar el problema anterior para que informe además, si existe por lo menos un artículo
    cuya cantidad sea igual a cero.
'''

i = 0
impares = 0

while True:
    print('---- Art. nuevo ----')
    cod = int(input('Ingrese el codigo del articulo: '))
    if cod == 0:
        break
    can = int(input('Ingrese la cantidad: '))
    imp = float(input('Ingrese el importe: '))
    fec = input('Ingrese la fecha: ')
    desc = input('Ingrese la descripcion: ')

    if cod % 2 != 0:
        impares += imp
        i += 1

    if can == 0:
        cantidad_cero = 1

promedio = (impares / i)

print(f'El promedio es: {promedio}')

if cantidad_cero == 1:
    print('Y existe un producto con cantidad igual a 0')