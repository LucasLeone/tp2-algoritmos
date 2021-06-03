'''
    Sabiendo los precios de costo de los artículos y la cantidad existente de cada artículo en un
    supermercado (deben ser leídos en forma de pares ordenados COSTO, CANTIDAD).
    obtener el valor total del stock que dicho supermercado posee. El alumno deberá
    establecer la condición para el fin de proceso.
'''

i = 0

total = 0

while i < 5:
    i+=1
    
    print('---- Producto nuevo ----')
    costo = float(input('Ingrese el costo del producto: $'))
    cantidad = int(input('Ingrese la cantidad del producto: '))

    producto = costo * cantidad

    total = total + producto

print(f'Hay un total de ${total} de stock')