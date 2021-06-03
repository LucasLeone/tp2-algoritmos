'''
    En un comercio dedicado a la venta de insumos informáticos, se quiere saber el importe
    recaudado a lo largo de un día de trabajo; para esto se dispone de toda la facturación de
    las ventas realizadas. Los datos de cada factura deben ser leídos en grupos (Número de
    factura, Número de vendedor, Importe de la venta); El proceso debe terminar al encontrar
    una facturación importe igual a cero.
'''

total = 0

# Un dia entero son 10 ventas
i = 0

while i < 10:
    i += 1

    factura = int(input('Ingrese el numero de factura: '))
    vendedor = int(input('Ingrese el numero del vendedor: '))
    importe = float(input('Ingrese el importe: $'))
    if importe == 0:
        break

    total += importe

print(f'En un dia se vendio un total de: ${total}')