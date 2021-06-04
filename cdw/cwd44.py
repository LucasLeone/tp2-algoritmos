'''
    Se dispone de una serie de ternas de números enteros y se quiere calcular e imprimir la suma
    de cada una de ellas indicando mediante un mensaje si dicha suma es múltiplo de nueve.
    Finalizar el proceso cuando una suma sea igual a cero.
'''

i = 0
suma = 0

while True:
    i += 1

    if i > 1 and suma == 0:
        break

    num1 = int(input('Ingrese el primer numero entero positivo: '))
    num2 = int(input('Ingrese el segundo numero entero positivo: '))
    num3 = int(input('Ingrese el tercer numero entero positivo: '))

    suma = num1 + num2 + num3

    if suma == 0:
        break
    
    if suma % 9 == 0:
        print(f'El total de la suma es: {suma} y ES MULTIPLO DE 9')
    else:
        print(f'El total de la suma es: {suma} y no es multiplo de 9')
