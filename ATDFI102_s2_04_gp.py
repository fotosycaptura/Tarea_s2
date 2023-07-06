"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
"""
import math as mt
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

def calcular_area_y_perimetro_triangulo(a: float, b: float, c: float)->list:
    resultado = []
    s = (a+b+c)/2.0
    perimetro = a+b+c
    area = mt.sqrt(s*(s-a)*(s-b)*(s-c))
    resultado.append(round(area, 2))
    resultado.append(perimetro)
    return resultado

lado_1 = pregunta_valor('Ingresa la longitud del primer lado: ')
lado_2 = pregunta_valor('Ingresa la longitud del segundo lado: ')
lado_3 = pregunta_valor('Ingresa la longitud del tercer lado: ')

area_perimetro = calcular_area_y_perimetro_triangulo(lado_1, lado_2, lado_3)

print(f'El área del triángulo es: {area_perimetro[0]} cms2')
print(f'El perímetro del triángulo es: {area_perimetro[1]} cms2')
