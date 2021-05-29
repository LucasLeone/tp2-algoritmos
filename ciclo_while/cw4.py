'''
    Se dispone de diez pares ordenados (X,y) de números. a los cuales se debe calcular la suma
    de todas las X y la suma de todas las Y, imprimir los resultados.
'''

i = 0
x = 0
y = 0

while i < 10:
    i = i+1
    print(f'Valores del {i} par ordenado')
    user_x = int(input('Ingrese el valor de X: '))
    user_y = int(input('Ingrese el valor de Y: '))
    x = x + user_x
    y = y + user_y

print(f'La suma de todas las X, Y es: {x}, {y}')