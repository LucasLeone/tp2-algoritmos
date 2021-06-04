'''
    Se dispone de una serie de cuaternas de números positivos y se quiere encontrar e imprimir la
    suma mayor de todas las cuaternas. El proceso finalizará cuando el primer elemento de
    alguna cuaterna sea igual a cero, luego de procesar esta.
'''

mayor = 0

while True:
    print('---- Nueva cuaterna ----')
    num1 = float(input('Ingrese el primer numero positivo: '))
    if num1 == 0:
        break
    num2 = float(input('Ingrese el segundo numero positivo: '))
    num3 = float(input('Ingrese el tercer numero positivo: '))
    num4 = float(input('Ingrese el cuarto numero positivo: '))

    suma = num1 + num2 + num3 + num4

    if suma == 0:
        break

    if mayor == 0:
        mayor = suma
    
    if suma >= mayor:
        mayor = suma

print(f'La suma mayor es: {mayor}')