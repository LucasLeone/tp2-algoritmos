'''
    En un comercio se quiere saber cuántos empleados realizaron ventas superiores a cien mil a
    lo largo un mes; para esto se dispone como dato del número de legajo, y el importe
    vendido por cada empleado durante el período controlado.
'''

ventas_superiores = 0

print('''
    Legajos disponibles:
        101
        102
        103
        104
''')

while True:
    print('---- Venta nueva ----')
    legajo = int(input('Ingrese el legajo del vendedor: '))
    if legajo == 0:
        break
    venta = float(input('Ingrese el valor de la venta $'))

    if venta > 10000:
