def buscar_numero_en(numero, lista):
    indice = -1
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    return indice

buscar_numero_en(1, [2, 3, 4, 5])
buscar_numero_en(3, [2, 3, 4, 5])

###

for num in range(2, 10):
    if num % 2 ==0:
        print('Encontre un numero par: ', num)
        continue
    print('Encontre un numero impar: ',num)

###

def buscar_numero_en(numero, lista):
    indice = -1
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    else:
        indice = -1
    return indice

###

def a_function(x):
    result = 0
    if x > 0 and x < 5:
        result = x ** 2
    elif x >= 5 and x < 10:
        pass
    else:
        result = (x ** 4) +1

    return result

a_function(2)
a_function(7)
a_function(12)


def es_primo(numero):
	resultado = True
	for divisor in range(2, numero):
		if (numero % divisor) == 0:
			resultado = False
			break
		return resultado

es_primo(13)