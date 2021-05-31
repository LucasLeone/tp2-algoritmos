'''
    Se dispone de una serie de temas de números enteros positivos y se quiere calcular e
    imprimir la suma de cada una de ellas, indicando mediante un mensaje si dicha suma es
    múltiplo de nueve. Finalizar el proceso cuando una suma sea igual a cero.
'''

while True:
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    num3 = int(input('Ingrese el tercer numero: '))

    if num1 < 0 or num2 < 0 or num3 < 0:
        break

    result = num1 + num2 + num3

    if result == 0:
        break

    print(f'La suma de {num1} + {num2} + {num3} es: {result}')

    if result % 9 == 0:
        print('Y ademas, es multiplo de 9')
