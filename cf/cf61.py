'''
    De una serie de 20 valores, se quiere saber cuántos cumplen con 
    la condición de ser impares mayores que cincuenta y menores que cien.
'''

numeros_condicionados = 0

for i in range(0, 20):
    num = int(input('Ingrese un numero: '))

    if num % 2 != 0:
        if num > 50 and num < 100:
            numeros_condicionados += 1

print(f'Hay un total de {numeros_condicionados} numeros impares mayores que 50 y menores que 100')