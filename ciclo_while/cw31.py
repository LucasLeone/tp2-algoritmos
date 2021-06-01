'''
    En la empresa MZZ', el gerente desea saber cuántos vendedores tienen una antigüedad
    superior a diez años; para poder realizar el proceso se dispone de los datos siguientes:
    legajo, sueldo y antigüedad (expresada en años). El proceso termina cuando algún legajo
    sea igual a cero.
'''

vendedores_antiguos = 0

while True:
    print('---- Nuevo empleado ----')
    legajo = int(input('Ingrese el numero del legajo: '))
    
    if legajo == 0:
        break

    sueldo = float(input('Ingrese el sueldo del empleado: $'))
    antiguedad = float(input('Ingrese los años de antiguedad del empleado: '))

    if antiguedad >= 10:
        vendedores_antiguos = vendedores_antiguos + 1

print(f'Hay {vendedores_antiguos} empleados con mas de 10 años de antiguedad')