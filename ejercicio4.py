# Solución Ejercicio 4: Analizador de contraseñas

password = input("Ingrese una contraseña: ")
tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
tiene_espacio = False


for caracter in password:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_numero = True
    elif caracter.isspace():
        tiene_espacio = True


longitud_valida = len(password) >= 8


criterios = 0
if longitud_valida:
    criterios = criterios + 1
if tiene_mayuscula:
    criterios = criterios + 1
if tiene_minuscula:
    criterios = criterios + 1
if tiene_numero:
    criterios = criterios + 1


if tiene_espacio or criterios <= 2:
    clasificacion = "Débil"
elif criterios == 3:
    clasificacion = "Aceptable"
elif criterios == 4:
    clasificacion = "Fuerte"

print(f"Longitud: {len(password)}")
print(f"Contiene mayúscula: {'Sí' if tiene_mayuscula else 'No'}")
print(f"Contiene minúscula: {'Sí' if tiene_minuscula else 'No'}")
print(f"Contiene número: {'Sí' if tiene_numero else 'No'}")
print(f"Contiene espacios: {'Sí' if tiene_espacio else 'No'}")
print(f"Criterios cumplidos: {criterios} de 4")
print(f"Clasificación: {clasificacion}")