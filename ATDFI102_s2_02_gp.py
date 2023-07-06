"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
----------------------------------------------------------------------
E2: Construye un programa en Python que calcule y muestre por pantalla 
la media aritmética (o promedio simple) de tres números ingresados 
por el usuario. El resultado deberá estar redondeado a 1 decimal.
"""

def pregunta_valor(msg: str)->float:
    valor = 0.0
    bl_resp = True
    while (bl_resp):
        try:
            valor =  float(input(msg))
            bl_resp = False
        except ValueError:
            print('Por favor ingrese un valor que sea numérico, o presione la tecla control más la tecla c para salir')
            bl_resp = True
    return valor

valor_1 = pregunta_valor('Ingrese el primer número: ')
valor_2 = pregunta_valor('Ingrese el segundo número: ')
valor_3 = pregunta_valor('Ingrese el tercer número: ')

promedio = (valor_1 + valor_2 + valor_3) / 3.0

print(f'El promedio es: {round(promedio, 1)}')