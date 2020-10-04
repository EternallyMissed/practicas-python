#'For' Itera sobre los items de cualquier secuencia, lista o
#cadena de texto en el orden en el que aparece.

palabras = ('gato', 'ventana', 'defenestrado')
for p in palabras:
    print(p, len(p))

for i in range(10):
    print(i)

marcas = ('sony', 'lenovo', 'samsung', 'nissan', 'masserati')
for p in marcas:
    print(p, len(p))
   
#'While' Sirve para repetir una o varias sentencias una cantidad 
# de veces, mientra se cumpla con una condicion

def suma_n(n):
    'suma los numeros de 1 a n'
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 1
    return result

suma_n(5)

def ciclo_infinito():
    'imprime el nu mero 1 infinitas veces'
    i = 1
    while 1 <= 10:
        print(i end=' ')

ciclo_infinito()
