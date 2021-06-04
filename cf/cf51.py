'''
    Leer una serie de 50 números enteros, informar mediante 
    un mensaje cuántos son mayores que 100.
'''

mayores = 0

for i in range(0, 50):
    num = int(input('Ingrese un numero entero: '))
    
    if num > 100:
        mayores += 1

print(f'Hay un total de {mayores} numeros mayores a 100')