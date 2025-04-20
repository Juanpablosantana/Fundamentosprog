# calculadora
print("Selecciones operacion")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
opcion = input("Ingrese la opcion deseada: ")
if opcion == "1":
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 + num2
    print("El resultado es: ", resultado)   
elif opcion == "2":
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 - num2
    print("El resultado es: ", resultado)   
elif opcion == "3":
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 * num2
    print("El resultado es: ", resultado)   
elif opcion == "4":
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if num2 == 0:
        print("Error: Division por cero")
    else:
        resultado = num1 / num2
        print("El resultado es: ", resultado)
elif opcion == "5":
    print("Salir de la calculadora")