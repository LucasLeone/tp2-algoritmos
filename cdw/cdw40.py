'''
    En un instituto de enseñanza, se quiere emitir un listado de todos aquellos alumnos que el
    promedio general sea superior a siete, para lo cual se ingresa como dato: número de legajo
    y los promedios de las cuatro materias que se dictan; verificar que cada promedio sea
    mayor que cero y menor que diez; si no cumple esta condición, Ignorar el valor lerdo y
    pedirlo nuevamente. Terminar el proceso cuando se lea un número de legajo igual a cero.
'''

alumnos_mayores = 0


while True:
    print('---- Nuevo alumno ----')
    legajo = int(input('Ingrese el numero de legajo: '))

    if legajo == 0:
        break


    promedio = float(input('Ingrese el promedio: '))

    if promedio < 0 or promedio > 10:
        print('Ingrese el promedio bien!!!')
        promedio = float(input('Ingrese el promedio: '))

    if promedio < 0 or promedio > 10:
        print('Volviste a poner mal el promedio. El programa se detiene!')
        break

    if promedio >= 7:
        alumnos_mayores += 1

print(f'Hay un total de {alumnos_mayores} alumnos con promedio mayor a 7')