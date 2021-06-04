'''
    Imprimir la sumatoria de todos los números pares comprendidos en el 
    intervalo veinte-cincuenta, (ambos inclusive). Resolverlo usando for y do-while.
'''

sumatoria = 0

while True:
    for i in range(20, 51):
        if i % 2 == 0:
            print(i)
            sumatoria += i
            

    if i == 50:
        break

print(f'La sumatoria es: {sumatoria}')