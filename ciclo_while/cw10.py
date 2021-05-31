'''
    En una oficina meteorológica se dispone de las temperaturas máximas y mínimas diarias, a
    lo largo de un período x. Se quieren encontrar las temperaturas mínima, máxima, la
    máxima de las mínimas y la mínima de las máximas. Se debe ingresar los datos de a pares
    ordenados (mín, max). El proceso termina cuando las temperaturas leídas sean (noventa y
    nueve - noventa y nueve).
'''

temp_max = 0
temp_min = 0
temp_min_de_max = 0
temp_max_de_min = 0

i = 0

while True:
    temp_min_day = float(input('Temperatura mínima del dia: '))
    temp_max_day = float(input('Temperatura máxima del dia: '))

    if i == 0:
        temp_max = temp_max_day
        temp_min = temp_min_day
        temp_max_de_min = temp_min_day
        temp_min_de_max = temp_max_day
        i = i + 1

    if temp_max_day and temp_min_day == 99:
        break

    if temp_max_day >= temp_max:
        temp_max = temp_max_day
    elif temp_min_day >= temp_min:
        temp_min = temp_min_day

    if temp_min_de_max >= temp_max_day:
        temp_min_de_max = temp_max_day
    elif temp_max_de_min <= temp_min_day:
        temp_max_de_min = temp_min_day


print(f'La temperatura minima fue: {temp_min}')
print(f'La temperatura maxima fue: {temp_max}')
print(f'La temperatura maxima de las minimas fue: {temp_max_de_min}')
print(f'La temperatura minima de las maximas fue: {temp_min_de_max}')