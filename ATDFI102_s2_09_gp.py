"""
Script creado por Xavier Fuentes.
Github: https://github.com/fotosycaptura
Codificado en Python 3.11.3
----------------------------------------
E9:
Construye un programa en Python que le
 pida al usuario su nombre y apellido 
 (en un solo ingreso), y le imprima por 
 pantalla la cantidad de letras que 
 poseen en total.
"""
entrada = input('Ingres tu primer nombre y apellido: ')
if (entrada != None and len(entrada) > 0):
    print(f'Tu nombre y apellido poseen {len(entrada.replace(" ", ""))} letras.')
else:
    print(f'El usuario no ha ingresado nada, saliendo...')