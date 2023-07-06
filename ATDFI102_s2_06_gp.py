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
            str_valor =  input(msg)

            if (len(str_valor) > 3):
                valor =int(str_valor)
                bl_resp = False
            else:
                print('Por favor ingrese un número de 4 cifras')
        except ValueError:
            print('Por favor ingrese un valor que sea numérico, o presione la tecla control más la tecla c para salir')
            bl_resp = True
    return valor

def descomponer(valor: int)->list:
    resultado = []
    valor_abs = valor
    if (valor < 0):
        valor_abs = abs(valor)
    
    miles = valor_abs // 1000

    if (valor < 0):
        miles  = miles * -1

    valor_abs %= 1000

    centenas = valor_abs // 100
    valor_abs %= 100

    decenas = valor_abs // 10
    unidades = valor_abs % 10

    resultado.append(miles)
    resultado.append(centenas)
    resultado.append(decenas)
    resultado.append(unidades)

    return resultado

numero = pregunta_valor('Ingresa un número de 4 cifras: ')
respuesta = descomponer(numero)
print(f'Descomposición: {respuesta[0]}M + {respuesta[1]}C + {respuesta[2]}D + {respuesta[3]}U')
