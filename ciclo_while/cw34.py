'''
    En un estadio de fútbol se quiere saber cuántas personas asistieron a presenciar un partido.
    En cada lectura se ingresarán la cantidad de personas que ingresaron por una de las veinte
    entradas, y el precio de la entrada. El proceso deberá concluir cuando el número de
    integrantes sea cero, o se complete la información de las veinte entradas, es decir
    ingresaron personas por todas las entradas posibles y no se permite mas ingreso.
'''

entradas = 0

total_personas = 0

while entradas < 20:
    entradas += 1
    personas = int(input('Cantidad de personas ingresadas por entrada: '))
    if personas == 0:
        break
    
    precio = float(input('Ingrese el valor de la entrada: $'))
    
    total_personas = total_personas + personas

print(f'Ingresaron un total de {total_personas} personas al estadio.')