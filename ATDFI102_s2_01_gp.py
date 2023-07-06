"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
"""
import math
try:
    numero = int(input('Ingrese un número: '))
    resultado = round(math.cbrt(numero), 2)

    print(f'La raíz cúbica de {numero} es {resultado}')
except ValueError:
    print('El texto que ingresó no era un número')
