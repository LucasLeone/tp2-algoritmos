'''
    Ingresar por teclado de a uno una serie de números. Encontrar e imprimir el 
    menor de los números pares. La cantidad de elementos leídos es cien.
'''

i = 0
menor = 0

while i < 100:
    num = int(input('Ingrese un numero: '))
    if i == 0 and num % 2 == 0:
        menor = num
    i = i + 1
    
    if num <= menor and num % 2 == 0:
        menor = num

print(f'El numero par menor encontrado es: {menor}')