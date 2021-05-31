'''
    Se dispone de una serie de ternas de números enteros positivos y se quiere calcular e
    imprimir la suma de cada una de ellas, indicando mediante un mensaje si dicha suma es
    Par. Fin de proceso cuando alguna suma sea mayor que setecientos.
'''

while True:
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    num3 = int(input('Ingrese el tercer numero: '))

    result = num1 + num2 + num3

    if result % 2 == 0:
        print(f'La suma de {num1} + {num2} + {num3} es: {result} y es par')
    else:
        print(f'La susuma de {num1} + {num2} + {num3} es: {result} y es inpar')

    if result > 700:
        break