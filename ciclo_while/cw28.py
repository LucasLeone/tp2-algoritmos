'''
    Leer una serie de números cuyo último valor es cero,
    se pide indicar cuántos valores hay mayores que cien.
'''

mayores = 0

print('El valor 0 frena el while')

while True:
    num = int(input('Ingrese un valor: '))
    if num == 0:
        break

    if num % 10 == 0 and num > 100:
        mayores = mayores + 1

print(f'Hay {mayores} numeros mayores de 100')