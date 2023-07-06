"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
----------------------------------------------------------------------------
E7: Construye un programa en Python que le pida al usuario un 
carácter cualquiera, y le muestre por pantalla el código ASCII 
que le corresponde a ese carácter.

Bueno, eso era lo original, yo le agregué que si agregas por ejemplo casa,
arroja cada caracter ASCII por cada letra de la palabra casa ;)
"""

entrada = input('Ingresa un caracter: ')
if (entrada != None and len(entrada) > 0):
    for letra in entrada:
        respuesta = ord(letra)
        print(f'El código ASCII de {letra} es: {respuesta}')
else:
    print('No se ingresó nada, saliendo.')
