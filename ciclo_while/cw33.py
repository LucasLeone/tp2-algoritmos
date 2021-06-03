'''
    En un local comercial recientemente se ha codificado la mercadería para su control; se quiere
    saber cuántos códigos impares mayores que cincuenta hay y cuáles son esos códigos
    mostrarlo por pantalla.. Los datos a ingresar son los siguientes: código del producto,
    importe, cantidad. fecha_última_compra. El proceso termina cuando el código leído sea
    igual a cero.
'''

codigos_impares_mayores = 0

while True:
    print('---- Producto nuevo ----')
    codigo = int(input('Ingrese el codigo del producto: '))
    if codigo == 0:
        break
    importe = float(input('Ingrese el valor del producto: $'))
    cantidad = int(input('Ingrese la cantidad: '))
    fecha_ultima_compra = input('Ingrese la fecha de la ultima compra: ')

    if codigo > 50 and codigo % 2 != 0:
        codigos_impares_mayores = codigos_impares_mayores + 1
        print(f'Codigo impar mayor a 50: {codigo}')

print(f'Hay un total de {codigos_impares_mayores} con codigo impar mayor a 50.')