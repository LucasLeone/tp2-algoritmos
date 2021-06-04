'''
    En un comercio se quiere saber el importe promedio de venta por vendedor. para ello se
    dispone de una lista con los datos de cada factura. NUM: Número de factura. FEC: Fecha de
    venta, VEN: Vendedor (oscila entre 1 y 4), CAN: Cantidad, PRE: precio unitario.
    Con los datos del problema anterior indicar el importe de la venta promedio de cada
    vendedor.
'''

ventas_totales = 0

ventas1 = 0
ventas2 = 0
ventas3 = 0
ventas4 = 0

vendido1 = 0
vendido2 = 0
vendido3 = 0
vendido4 = 0

# El proceso termina cuando el numero de factura es igual a 0 o el vendedor es erroneo
while True:
    print('---- Nuevo proceso ----')
    num = int(input('Ingrese el numero de factura: '))
    if num == 0:
        break

    fec = input('Ingrese la fecha: ')
    ven = int(input('Ingrese el numero de vendedor (entre 1 y 4): '))
    if ven > 4 or ven < 1:
        print('Vendedor erroneo')
        break

    can = int(input('Ingrese la cantidad: '))

    total = 0
    for num in range(0, can):
        pre = int(input('Ingrese el precio unitario: $'))
        total = total + pre

    if ven == 1:
        vendido1 += total
        ventas1 += 1
    elif ven == 2:
        vendido2 += total
        ventas2 += 1
    elif ven == 3:
        vendido3 += total
        ventas3 += 1
    elif ven == 4:
        vendido4 += total
        ventas4 += 1

    ventas_totales += 1


if ventas_totales >= 1:
    if ventas1 >= 1:
        promedio1 = (vendido1 / ventas1)
        print(f'El promedio vendido por el vendedor 1 es: {promedio1}')
    
    if ventas2 >= 1:
        promedio2 = (vendido2 / ventas2)
        print(f'El promedio vendido por el vendedor 2 es: {promedio2}')
    
    if ventas3 >= 1:
        promedio3 = (vendido3 / ventas3)
        print(f'El promedio vendido por el vendedor 3 es: {promedio3}')
    
    if ventas4 >= 1:
        promedio4 = (vendido4 / ventas4)
        print(f'El promedio vendido por el vendedor 4 es: {promedio4}')
