'''
    De una serie de números que se leerán por teclado. Calcular el promedio de los números
    pares cuyo número de orden sea impar, informar además por única vez si existen números
    negativos entre los números pares, en dicho caso. Ignorar el número leído y continuar con
    los restantes. Terminar el proceso cuando la suma de los números impares encontrados en la
    serie sea mayor que mil.
'''

suma_mayor = 0
i = 0
totalpares = 0
promedio = 0
existen_neg = False

while suma_mayor < 1000:
    i += 1

    print('---- Nuevo numero ----')
    num = int(input('Ingresar un numero: '))

    if num % 2 == 0:
        if num < 0:
            existen_neg = True
            pass
        if i % 2 != 0:
            totalpares += num
            promedio += 1
        
    if num % 2 != 0:
        suma_mayor += num
       
    

print(f'El promedio de los numeros pares con orden impar es: {totalpares / promedio}')

if existen_neg == True:
    print('Tambien existen numeros negativos dentro de la serie')

print(f'Y la suma de los numeros impares es: {suma_mayor}')