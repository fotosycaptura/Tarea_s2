"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
"""

entrada = input('Ingresa un caracter: ')
if (entrada != None and len(entrada) > 0):
    for letra in entrada:
        respuesta = ord(letra)
        print(f'El código ASCII de {letra} es: {respuesta}')
else:
    print('No se ingresó nada, saliendo.')
