'''
    Se dispone de cincuenta pares ordenados (X.Y) de números. a los cuáles se debe calcular la
    suma de todos las X y la suma de todas las Y; imprimir los resultados
'''

sumax = 0
sumay = 0

for i in range(0, 50):
    x = int(input('Ingrese el primer valor: '))
    y = int(input('Ingrese el segundo valor: '))

    sumax += x
    sumay += y

print(f'La suma de x: {sumax}')
print(f'La suma de y: {sumay}')