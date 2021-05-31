'''
    Ídem al problema anterior, pero esta vez, el fin del proceso 
    está dado cuando el importe mayor supere los mil.
'''

# Codigos de vendedores
vendedor1 = 1
venta_mayor_1 = 0
venta_menor_1 = 0

vendedor2 = 2
venta_mayor_2 = 0
venta_menor_2 = 0

vendedor3 = 3
venta_mayor_3 = 0
venta_menor_3 = 0

vendedor4 = 4
venta_mayor_4 = 0
venta_menor_4 = 0

i = 0

while True:
    i = i + 1

    cod_vendedor = int(input('Que vendedor fue? '))
    if cod_vendedor != 1 and cod_vendedor != 2 and cod_vendedor != 3 and cod_vendedor != 4:
        print('codigo erroneo')
        break
    venta = float(input('Ingrese el importe: '))


    if i == 1:
        venta_menor_1 = venta
        venta_menor_2 = venta
        venta_menor_3 = venta
        venta_menor_4 = venta
        

    if cod_vendedor == 1:
        if venta > venta_mayor_1:
            venta_mayor_1 = venta
        if venta < venta_menor_1:
            venta_menor_1 = venta

    elif cod_vendedor == 2:
        if venta > venta_mayor_2:
            venta_mayor_2 = venta
        if venta < venta_menor_2:
            venta_menor_2 = venta

    elif cod_vendedor == 3:
        if venta > venta_mayor_3:
            venta_mayor_3 = venta
        if venta < venta_menor_3:
            venta_menor_3 = venta

    elif cod_vendedor == 4:
        if venta > venta_mayor_4:
            venta_mayor_4 = venta
        if venta < venta_menor_4:
            venta_menor_4 = venta
            
    else:
        print('CODIGO DE VENDEDOR ERRONEO')

    if venta > 1000:
        break

    continua = input('Continua? s/n ')
    continua = continua.lower()

    if continua == 's':
        continue
    else:
        break


venta_mayor = 0
venta_menor = 0
vendedor_mayor = 0
vendedor_menor = 0

if venta_mayor_1 > venta_mayor_2 and venta_mayor_1 > venta_mayor_3 and venta_mayor_1 > venta_mayor_4:
    venta_mayor = venta_mayor_1
    vendedor_mayor = 1
elif venta_mayor_2 > venta_mayor_1 and venta_mayor_2 > venta_mayor_3 and venta_mayor_2 > venta_mayor_4:
    venta_mayor = venta_mayor_2
    vendedor_mayor = 2
elif venta_mayor_3 > venta_mayor_1 and venta_mayor_3 > venta_mayor_2 and venta_mayor_3 > venta_mayor_4:
    venta_mayor = venta_mayor_3
    vendedor_mayor = 3
elif venta_mayor_4 > venta_mayor_1 and venta_mayor_4 > venta_mayor_2 and venta_mayor_4 > venta_mayor_3:
    venta_mayor = venta_mayor_4
    vendedor_mayor = 4

if venta_menor_1 < venta_menor_2 and venta_menor_1 < venta_menor_3 and venta_menor_1 < venta_menor_4:
    venta_menor = venta_menor_1
    vendedor_menor = 1
elif venta_menor_2 < venta_menor_1 and venta_menor_2 < venta_menor_3 and venta_menor_2 < venta_menor_4:
    venta_menor = venta_menor_2
    vendedor_menor = 2
elif venta_menor_3 < venta_menor_1 and venta_menor_3 < venta_menor_2 and venta_menor_3 < venta_menor_4:
    venta_menor = venta_menor_3
    vendedor_menor = 3
elif venta_menor_4 < venta_menor_1 and venta_menor_4 < venta_menor_2 and venta_menor_4 < venta_menor_3:
    venta_menor = venta_menor_4
    vendedor_menor = 4

print(f'La venta mayor la hizo el vendedor {vendedor_mayor} y fue de ${venta_mayor}')
print(f'La venta menor la hizo el vendedor {vendedor_menor} y fue de ${venta_menor}')