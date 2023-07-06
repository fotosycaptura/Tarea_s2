"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
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

def calcular_area_trapecio(BS: float, BI: float, H: float)->float:
    return round((BS+BI)/2 *H, 3)

base_superior = pregunta_valor('Ingresa la longitud en cms de la base superior: ')
base_inferior = pregunta_valor('Ingresa la longitud en cms de la base inferior: ')
altura = pregunta_valor('Ingresa la altura en cms: ')

print(f'El área del trapecio es: {calcular_area_trapecio(base_superior, base_inferior, altura)} cms2')
