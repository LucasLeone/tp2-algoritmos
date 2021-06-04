'''
    Se dispone de una serie de ternas de números enteros positivos y se quiere calcular e imprimir
    la suma de cada una de ellas indicando mediante un mensaje sí dicha suma es Par. Fin de
    proceso cuando la suma de alguna terna sea mayor que setecientos.
'''

suma = 0

while True:
    if suma > 700:
        break

    num1 = int(input('Ingrese el primer numero entero positivo: '))
    num2 = int(input('Ingrese el segundo numero entero positivo: '))
    num3 = int(input('Ingrese el tercer numero entero positivo: '))

    total = num1 + num2 + num3

    if total % 2 == 0:
        print(f'El total de la suma es: {total} y es una suma par')
    else:
        print(f'El total de la suma es: {total} y no es una suma par')
    
    suma = total