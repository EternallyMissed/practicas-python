numeros = range(101)
suma_pares = 0
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]
    i += 1

print('Suma de todos los valores pares que hay en el rango 1-100', suma_pares)