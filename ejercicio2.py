# Solución Ejercicio 2
cantidad = int(input("¿Cuántos números desea analizar?: "))

if cantidad <= 0:
    print("Error: la cantidad debe ser un entero mayor que cero.")
else:
    positivos = 0
    negativos = 0
    ceros = 0
    suma_total = 0.0

    for i in range(1, cantidad + 1):
        numero = float(input(f"Ingrese el número {i}: "))
        suma_total += numero

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

    promedio = suma_total / cantidad

    print(f"Cantidad de positivos: {positivos}")
    print(f"Cantidad de negativos: {negativos}")
    print(f"Cantidad de ceros: {ceros}")
    
    if suma_total.is_integer():
        print(f"Suma total: {int(suma_total)}")
    else:
        print(f"Suma total: {suma_total:.2f}")
        
    print(f"Promedio: {promedio:.2f}")