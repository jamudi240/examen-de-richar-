lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Error: todos los lados deben ser mayores que cero.")
else:

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Los lados ingresados forman un triángulo válido.")
        
        # Clasificación anidada según sus lados
        if lado1 == lado2 and lado2 == lado3:
            print("Tipo de triángulo: equilátero.")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Tipo de triángulo: isósceles.")
        else:
            print("Tipo de triángulo: escaleno.")
    else:
        print("Los lados ingresados forman un triángulo valido .")

