"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
"""
def pregunta_valor(msg: str, minimo: int, largo: int, tipo: str)->int:
    valor = 0.0
    bl_valido = False
    while (not bl_valido):
        try:
            entrada =  int(input(msg))

            # Valida que el valor ingresado esté entre el mínimo y máximo en largo de caracteres. 
            if (str(entrada) != None and (len(str(entrada)) >= minimo and len(str(entrada)) <= largo)):
                # Es válido, pero si largo es 2, debería de validarse si el número va de 1 hasta 12 - meses del año -
                # y para los días de 1 hasta 31
                
                match tipo:
                    case 'D':
                        if(entrada >= 1 and entrada <= 31):
                            valor = entrada
                            bl_valido = True
                        else:
                            print('Valor para día no válido.')
                    case 'M':
                        if(entrada >= 1 and entrada <= 12):
                            valor = entrada
                            bl_valido = True
                        else:
                            print('Valor para mes no válido.')
                    case 'YYYY':
                        valor = entrada
                        bl_valido = True
                    case _:
                        print('Valor no válido.')

            else:
                print(f'Se esperaba un número de {largo} caracteres.')
        except ValueError:
            print('Por favor ingrese un valor que sea numérico, o presione la tecla control más la tecla c para salir')
            bl_resp = True
    return valor

dia = pregunta_valor('Ingrese el día de tu nacimiento: ', 1, 2, 'D')
mes = pregunta_valor('Ingrese el mes de tu nacimiento: ', 1, 2, 'M')
anio = pregunta_valor('Ingresa el año de tu nacimiento: ', 4, 4, 'YYYY')

print(f'Naciste el {dia}-{mes}-{anio}')