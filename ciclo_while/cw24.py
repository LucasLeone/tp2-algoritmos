'''
    Se dispone de una serie de cuaternas de números positivos y se quiere encontrar e imprimir
    la suma mayor de todas las cuaternas. El proceso finalizará cuando el primer elemento de
    alguna cuaterna sea igual a cero.
'''

i = 0
mayor = 0

while True:
    print('---- Nueva cuaterna ----')
    num1 = int(input('Ingrese el primer numero: '))
    if num1 == 0:
        break
    num2 = int(input('Ingrese el segundo numero: '))
    num3 = int(input('Ingrese el tercer numero: '))
    num4 = int(input('Ingrese el cuarto numero: '))

    if num1 < 0 or num2 < 0 or num3 < 0 or num4 < 0:
        break

    result = num1 + num2 + num3 + num4

    if i == 0:
        mayor = result
        i = i + 1

    if result >= mayor:
        mayor = result
        

if i != 0:
    print(f'La mayor suma de las cuaternas es: {mayor}')
else:
    quit()