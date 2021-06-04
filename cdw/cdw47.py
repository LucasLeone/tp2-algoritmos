'''
    Leer una serie de pares ordenados; indicando cuántos contienen múltiples de dos en sus
    primeros componentes; y de cinco, en las segundas Componentes. Terminar el
    proceso cuando las componentes X e Y de algún par sean múltiples de tres.
'''

multiplos2 = 0
multiplos5 = 0

while True:
    x = int(input('Ingrese el primer valor: '))
    y = int(input('Ingrese el segundo valor: '))

    if x % 3 == 0 or y % 3 == 0:
        print('Son multiplos de 3')
        break

    if x % 2 == 0:
        multiplos2 += 1
    
    if y % 5 == 0:
        multiplos5 += 1

print(f'Hay un total de {multiplos2} numeros que son multiplos de 2')
print(f'Hay un total de {multiplos5} numeros que son multiplos de 5')