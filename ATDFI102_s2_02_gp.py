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