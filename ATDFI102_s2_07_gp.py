

entrada = input('Ingresa un caracter: ')
if (entrada != None and len(entrada) > 0):
    for letra in entrada:
        respuesta = ord(letra)
        print(f'El código ASCII de {letra} es: {respuesta}')
else:
    print('No se ingresó nada, saliendo.')
