'''
    De una serie de números que se leerán por teclado. Calcular el promedio de los números
    pares cuyo número de orden sea impar, informar además por única vez si existen números
    negativos entre los números pares, en dicho caso. Ignorar el número leído y continuar con
    los restantes. Terminar el proceso cuando la suma de los números impares encontrados en la
    serie sea mayor que mil.
'''

suma_mayor = 0
i = 0
promedio = 0

while suma_mayor < 1000:
    i += 1

    num = int(input('Ingrese un valor: '))
    if num < 0:
        print('Numero negativo!')
        pass
    
    if num % 2 == 0 and i % 2 != 0:
        num_impar = num
        promedio = promedio + num_impar

    if num % 2 != 0:
        suma_mayor += num

    print(i)

print(f'El promedio es: {promedio / i}')
print(f'La suma de los numeros impares es: {suma_mayor}')