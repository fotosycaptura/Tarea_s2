"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
---------------------------------------------------------------------------
E5: Construye un programa en Python que calcule y muestre por pantalla el 
perímetro de la circunferencia, el área del círculo, y el volumen de 
la esfera, que se pueden construir a partir del radio ingresado por el 
usuario. Utiliza a  con el valor 3.141593 y redondea los resultados a 2 
decimales de precisión.
El perímetro de la circunferencia corresponde al cálculo 2*pi*radio, 
el área del círculo es pi*radio^2, 
y el volumen de la esfera se calcula como (4*pi*radio^3)/3.
"""
import math as mt

def pregunta_valor(msg: str)->float:
    valor = 0.0
    bl_resp = True
    while (bl_resp):
        try:
            valor =  float(input(msg))
            if valor > 0:
                bl_resp = False
            else:
                print('Por favor ingrese un número mayor que cero')
        except ValueError:
            print('Por favor ingrese un valor que sea numérico, o presione la tecla control más la tecla c para salir')
            bl_resp = True
    return valor

def calculos(r: float)->list:
    resultado = []
    pi = 3.141593
    perimetro = 2*pi*r
    area = pi*r**2
    volumen = (4*pi*r**3)/3
    resultado.append(round(perimetro, 2))
    resultado.append(round(area, 2))
    resultado.append(round(volumen, 2))
    return resultado

radio = pregunta_valor('Ingresa el radio: ')
perimetro_area_volumen = calculos(radio)

print(f'El perímetro del cículo es: {perimetro_area_volumen[0]} cms')
print(f'El área de la circunferencia es: {perimetro_area_volumen[1]} cms2')
print(f'El volumen de la esfera es: {perimetro_area_volumen[2]} cms3')
