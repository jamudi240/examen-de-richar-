import math
opcion = ""
while opcion != "4":
    print("\n--- CALCULADORA GEOMÉTRICA ---")
    print("1. Área de un círculo")
    print("2. Calcular hipotenusa")
    print("3. Resolver ecuación cuadrática")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        radio = float(input("Ingrese el radio: "))
        if radio < 0:
            print("Error: El radio debe ser mayor o igual que cero.")
        else:
            area = math.pi * (radio ** 2)
            print(f"Área del círculo: {area:.2f}")
            
    elif opcion == "2":
        cateto1 = float(input("Ingrese el primer cateto: "))
        cateto2 = float(input("Ingrese el segundo cateto: "))
        if cateto1 <= 0 or cateto2 <= 0:
            print("Error: Los catetos deben ser mayores que cero.")
        else:
            hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
            print(f"Hipotenusa: {hipotenusa:.2f}")
            
    elif opcion == "3":
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        
        if a == 0:
            print("No es una ecuación cuadrática (a no puede ser cero).")
        else:
            discriminante = (b ** 2) - (4 * a * c)
            
            if discriminante > 0:
                x1 = (-b + math.sqrt(discriminante)) / (2 * a)
                x2 = (-b - math.sqrt(discriminante)) / (2 * a)
                print(f"Primera solución: {x1:.2f}")
                print(f"Segunda solución: {x2:.2f}")
            elif discriminante == 0:
                x = -b / (2 * a)
                print(f"Solución única: {x:.2f}")
            else:
                print("No existen soluciones reales.")
                
    elif opcion == "4":
        print("Programa finalizado.")
        
    else:
        print("Opción inválida. Intente de nuevo.")