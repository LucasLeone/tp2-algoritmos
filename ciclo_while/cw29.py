'''
    En una empresa se desea saber cuántos empleados tienen un sueldo superior a mil. Se
    dispone como dato el número del legajo y el sueldo de cada uno de los empleados. El
    proceso termina cuando el número de legajo lerdo sea igual a cero.
'''

sueldo_superior = 0

while True:
    print('---- Empleado nuevo ----')
    legajo = int(input('Ingrese el legajo del empleado: '))
    if legajo == 0:
        break

    sueldo = float(input('Ingrese el sueldo: $'))

    if sueldo > 1000:
        sueldo_superior = sueldo_superior + 1

print(f'Hay un total de {sueldo_superior} empleados que cobran mas de mil')