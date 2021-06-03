'''
    En un cine se quiere saber cuánto se recaudó a lo largo de un día, sabiendo que el valor de la
    entrada es de tres pesos,. que existen tres puertas de acceso y en el cine hay tres funciones
    diarias TA: tarde; NO: noche y TN: trasnoche. En cada lectura ingresarán el número de
    puerta por el que ingresaron los espectadores, la cantidad de entradas vendidas y el código
    de la función. El fin de proceso queda él cargo del alumno.
'''

recaudado = 0

i = 0

print('''
    Puertas:
        TA: Tarde [1]
        NO: Noche [2]
        TN: Trasnoche [3]
''')

while i < 5:
    i += 1

    print('---- Pelicula nueva ----')
    puerta = int(input('Ingrese el numero de la puerta: '))
    if puerta > 3 or puerta < 1:
        print('Puerta incorrecta')
        break

    entradas = int(input('Ingrese la cantidad de entradas vendidas: '))
    codigo = int(input('Ingrese el codigo de la funcion: '))

    recaudado = recaudado + (entradas * 3)

print(f'El total recaudado fue: ${recaudado}')