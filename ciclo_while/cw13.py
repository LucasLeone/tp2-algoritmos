'''
    Leer un número calcular la raíz cúbica y así sucesivamente hasta que el resultado sea menor
    o igual qué uno, imprimir los resultados parciales y finales. Controlar que el número Ieido
    sea mayor que cero al comenzar el proceso.
'''
# INSTALAR NUMPY EN SU ENTORNO PARA QUE FUNCIONE
import numpy as np


while True:
    num = int(input('Ingrese un número: '))

    if num < 0:
        print('El numero es menor que 0')
        break

    r_cub = np.cbrt(num)
    print(f'La raiz cubica de {num} es: {r_cub}')

    r_cub = np.cbrt(r_cub)
    
    if r_cub <= 1:
        break
    