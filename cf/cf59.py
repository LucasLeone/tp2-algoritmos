'''
    Se leen de a una, una serie las sumas doscientas ternas de números enteros y positivos.
    se quiere encontrar e imprimir la suma menor de todas las sumas impares.
'''

menor = 0

for i in range(0, 200):
    print('---- Nueva terna ----')
    num1 = int(input('Ingrese el primer numero entero positivo: '))
    num2 = int(input('Ingrese el segundo numero entero positivo: '))
    num3 = int(input('Ingrese el tercer numero entero positivo: '))

    suma = num1 + num2 + num3

    if suma % 2 != 0:
        if menor == 0:
            menor = suma
        elif suma < menor:
            menor = suma

print(f'La suma menor fue: {menor}')