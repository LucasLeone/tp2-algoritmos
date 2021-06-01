'''
    Se dispone de una serie de cuaternas de numeras positivos y se quiere encontrar e imprimir
    la suma mayor, de todas las cuaternas. El proceso terminará cuando alguna suma sea impar.
'''

i = 0
mayor = 0

while True:
    print('---- Nueva Cuaterna ----')
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    num3 = int(input('Ingrese el tercer numero: '))
    num4 = int(input('Ingrese el cuarto numero: '))

    if num1 < 0 or num2 < 0 or num3 < 0 or num4 < 0:
        print('Ingresaste un numero negativo')
        break

    results = num1 + num2 + num3 + num4

    if i == 0:
        mayor = results

    if results >= mayor:
        mayor = results
    
    if results % 2 != 0:
        print('La ultima suma de la cuaterna dio un numero impar')
        break

print(f'La suma de las cuaternas mayor fue: {mayor}')