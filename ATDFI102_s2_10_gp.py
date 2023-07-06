"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
----------------------------------------
E10:
Construye un programa en Python que 
permita transformar a segundos una 
cantidad de días, horas, minutos y 
segundos, que ingrese el usuario
"""
def pregunta_valor(msg: str)->int:
    valor = 0.0
    bl_resp = True
    while (bl_resp):
        try:
            valor =  int(input(msg))
            if valor >= 0:
                bl_resp = False
            else:
                print('Por favor ingrese un número mayor o igual que cero')
        except ValueError:
            print('Por favor ingrese un valor que sea numérico positivo, o presione la tecla control más la tecla c para salir')
            bl_resp = True
    return valor

def calculos(dias, horas, minutos, segundos)->int:
    total_segundos = 0
    total_segundos = segundos
    total_segundos += minutos * 60
    total_segundos += horas * 3600
    total_segundos += dias * 86400
    return total_segundos

dias = pregunta_valor('Ingresa la cantidad de días: ')
horas = pregunta_valor('Ingresa la cantidad de horas: ')
minutos = pregunta_valor('Ingresa la cantidad de minutos: ')
segundos = pregunta_valor('Ingresa la cantidad de segundos: ')

print(f'La cantidad equivalente es {calculos(dias, horas, minutos, segundos)} segundos.')
