print("Bienvenido al sistema de venta de entradas")
entradas_disponibles = 10
while True:
    try:
        opcion =  int(input("\nSeleccione una opción:\n1. Comprar entradas\n2. consultar disconibilidad\n3. Salir\nseleccione una opción: "))
        if opcion == 1:
            cantidad = int(input("Ingrese la cantidad de entradas que desea comprar: "))
            if 0 < cantidad <= entradas_disponibles:
                entradas_disponibles -= cantidad
                print(f"Compra exitosa. Entradas restantes: {entradas_disponibles}")
            else:
                print("Cantidad no válida. Intente de nuevo.")
        elif opcion == 2:
            print(f"Entradas disponibles: {entradas_disponibles}")
        elif opcion == 3:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")