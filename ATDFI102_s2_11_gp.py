"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
----------------------------------------
E11:
Construye un programa en Python que 
calcule y muestre el sueldo neto de un 
trabajador, a partir de las horas 
trabajadas y del pago por hora que le 
corresponde, ambos ingresados por el 
usuario. El sueldo base se calcula como 
horas trabajadas por el pago por hora, 
a ese monto, le debes agregar un 25% por
 concepto de beneficios, realizar un 10%
de descuentos, y descontar un 5% de 
los beneficios por concepto de 
consignación. 
El resultado debe estar aproximado al 
entero superior.
"""

import math as mt

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

def calculos(horas_trabajadas, valor_hora)->int:
    sueldo_base = horas_trabajadas * valor_hora
    beneficios = sueldo_base * 0.25
    descuentos = sueldo_base * 0.10
    consignacion = beneficios * 0.05
    Total = sueldo_base + beneficios - descuentos - consignacion
    return mt.trunc(round(Total, 0))

horas_trabajadas = pregunta_valor('Ingresa las horas trabajadas: ')
valor_hora = pregunta_valor('Ingresa el valor hora en $: ')
sueldo_neto = calculos(horas_trabajadas, valor_hora)

print(f'El sueldo neto mensual será de ${sueldo_neto} pesos.')
