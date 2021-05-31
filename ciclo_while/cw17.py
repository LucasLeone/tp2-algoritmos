'''
    Leer un número y si es múltiplo de cuatro sin serlo de cinco, calcular los diez primeros
    múltiplos de dicho número, sino su mitad, tercera y cuarta parte, imprimiendo los valores
    mientras se calculan.
'''

while True:
    num = int(input('Ingrese un numero: '))
    if num == 0:
        break

    if num % 4 == 0 and num % 5 != 0:
        print(f'Los primeros 10 multiplos de {num} son:')
        print(f'''
            {num * 2}
            {num * 3}
            {num * 4}
            {num * 5}
            {num * 6}
            {num * 7}
            {num * 8}
            {num * 9}
            {num * 10}
            {num * 11}
        ''')
    else:
        print(f'La mitad, tercer y cuarta parte de {num} es: ')
        print(f'''
            {num / 2}
            {num / 3}
            {num / 4}
        ''')