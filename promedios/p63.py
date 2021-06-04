'''
    Informar cuantos números negativos fueron ingresados por
    teclado. El fin de proceso lo define el programador.
'''

# Fin del proceso cuando i > 10

i = 0
negativos = 0

while i < 10:
    i += 1

    num = int(input('Ingrese un numero: '))

    if num < 0:
        negativos += 1


print(f'Se ingresaron un total de {negativos} numeros negativos')