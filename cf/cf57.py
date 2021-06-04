'''
    Ingresar por teclado de a uno una serie de números. Encontrar e imprimir
    el menor de los números pares. La cantidad de elementos lerdos es cien.
'''

menor = 0

for i in range(0, 100):
    x = int(input('Ingrese el primer valor: '))

    if x % 2 == 0:
        if x == 0:
            pass
        elif i == 0:
            menor = x
        elif x < menor:
            menor = x

print(f'El numero par menor es: {menor}')