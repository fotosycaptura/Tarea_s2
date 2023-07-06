"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
--------------------------------------------------------------------------------------------------------------
E12:
Construye un programa en Python que le permita a un alumno de una asignatura conocer su 
Nota de Presentación a Examen (NPE) y la nota mínima que necesita en el examen para aprobarla.

Considera las siguientes ponderaciones de las diversas evaluaciones del alumno, para calcular 
la NPE: la primera solemne pondera un 20%, la segunda solemne pondera un 25%, la tercera 
solemne pondera un 30% y el promedio de 3 controles pondera un 25%. Entonces, la NPE se calcula 
así:
NPE = Solemne_1 * 0.2 + Solemne_2 * 0.25 + Solemne_3 * 0.3 + ( (Control_1 + Control_2 + Control_3)/3) * 0.25 

Para calcular la nota mínima en el examen que necesita el alumno para aprobar, considera que la nota final de 
la asignatura se calcula así: la NPE pondera un 70% y la nota del examen pondera un 30%. De esta forma, la 
nota mínima que necesita el alumno para aprobar obedece al siguiente cálculo:

Nota Examen = (4 - NPE * 0.7)/0.3

"""

import math as mt

def pregunta_valor(msg: str)->float:
    valor = 0.0
    bl_resp = True
    while (bl_resp):
        try:
            valor =  float(input(msg))
            if valor >= 1.0 and valor <= 7.0:
                bl_resp = False
            else:
                print('Por favor ingrese un número entre 1.0 y 7.0')
        except ValueError:
            print('Por favor ingrese un número entre 1.0 y 7.0, o presione la tecla control más la tecla c para salir')
            bl_resp = True
    return valor

def calculos(n1: float, n2: float, n3: float, cl1: float, cl2: float, cl3: float)->list:
    resultado = []
    NPE = round(n1 * 0.2 + n2 * 0.25 + n3 * 0.3 + ( (cl1 + cl2 + cl3)/3) * 0.25, 1)
    NE = round((4 - NPE * 0.7) / 0.3, 1)

    resultado.append(NPE)
    resultado.append(NE)

    return resultado

n1 = pregunta_valor('Ingresa nota solemne 1: ')
n2 = pregunta_valor('Ingresa nota solemne 2: ')
n3 = pregunta_valor('Ingresa nota solemne 3: ')
print('')
cl1 = pregunta_valor('Ingresa nota control 1: ')
cl2 = pregunta_valor('Ingresa nota control 2: ')
cl3 = pregunta_valor('Ingresa nota control 3: ')

nota_presentacion_y_minima = calculos(n1, n2, n3, cl1, cl2, cl3)
print('')
print(f'La nota de presentación a examen es: {nota_presentacion_y_minima[0]}')
print(f'La nota mínima que debe obtener en el examen es: {nota_presentacion_y_minima[1]}')

