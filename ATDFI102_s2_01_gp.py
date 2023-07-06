import math
try:
    numero = int(input('Ingrese un número: '))
    resultado = round(math.cbrt(numero), 2)

    print(f'La raíz cúbica de {numero} es {resultado}')
except ValueError:
    print('El texto que ingresó no era un número')
