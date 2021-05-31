'''
    Ingresando un número como dato, imprimir de sus primeros cincuenta múltiplos,
    que no sean a la vez múltiples de seis.
'''

num = int(input('Ingrese un numero: '))

i = 0

while i < 50:
    i = i + 1
    multiplo = num * i

    if multiplo % 6 != 0:
        print(multiplo)