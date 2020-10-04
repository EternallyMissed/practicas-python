import random
input('Bienvenido/a, presione cualquier tecla para comenzar.')
while True:
    input('Presione una tecla para lanzar el primer dado!')
    a = random.randint(1, 6)
    print('El primer dado obtuvo un', a)
    input('Presione una tecla para lanzar el segundo dado!')
    b = random.randint(1, 6)
    print('El segundo dado obtuvo un', b)

    resultado = a+b
    print('La suma de ambos dados es:', resultado)
    respuesta = input('¿Quieres volver a lanzar? S/N')
    if respuesta in ('s', 'S', 'si', 'Si', 'SI'):
        respuesta = True
    elif respuesta in ('n', 'N', 'no', 'No', 'NO'):
        break
    else:
        print('Gracias por jugar!')
        respuesta = False
