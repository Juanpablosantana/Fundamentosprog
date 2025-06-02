print("Calculadora de área de triángulos")

triangulos = int(input("¿Cuantos Triangulos desea calcular?: "))
for i in range(triangulos):
    try:
        base = float(input(f"Ingrese la base del triángulo: "))
        altura = float(input(f"Ingrese la altura del triángulo: "))
        
        if base > 0 and altura > 0:
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area}")
        else:
            print("La base y la altura deben ser mayores que cero. Intente de nuevo.")
    except ValueError:
        print("Error. Por favor, ingrese un número válido para la base y la altura.")
     