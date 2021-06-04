'''
    Se dispone de una serie de cuaternas de números positivos y se quiere encontrar e imprimir la
    suma mayor de todas las cuaternas. Se procesarán quinientas cuaternas
'''

mayor = 0

for i in range(0, 500):
    print('---- Nueva cuaterna ----')
    num1 = int(input('Ingrese el primer numero positivo: '))
    num2 = int(input('Ingrese el segundo numero positivo: '))
    num3 = int(input('Ingrese el tercer numero positivo: '))
    num4 = int(input('Ingrese el cuarto numero positivo: '))

    suma = num1 + num2 + num3 + num4

    if suma > mayor:
        mayor = suma

print(f'La suma mayor es: {mayor}')