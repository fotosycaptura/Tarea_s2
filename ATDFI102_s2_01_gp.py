"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
----------------------------------------------------------------------
E1: Construye un programa en Python que calcule y muestre por pantalla
la raíz cúbica de un número entero ingresado por el usuario. 
El resultado deberá estar redondeado a 2 decimales.

"""
import math
try:
    numero = int(input('Ingrese un número: '))
    resultado = round(math.cbrt(numero), 2)

    print(f'La raíz cúbica de {numero} es {resultado}')
except ValueError:
    print('El texto que ingresó no era un número')
