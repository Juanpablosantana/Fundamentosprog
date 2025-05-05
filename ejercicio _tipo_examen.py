import random

# Pedir al usuario los límites
a = int(input("Ingrese el límite inferior: "))
b = int(input("Ingrese el límite superior: "))

# Generar número aleatorio
numero = random.randint(a, b)
print(f"Número aleatorio generado: {numero}")

# Pedir porcentaje
porcentaje = int(input("Ingrese el porcentaje: "))

# Pedir operación
operacion = input("¿Desea sumar (+) o restar (-) el porcentaje?: ")

# Calcular resultado
if operacion == "+":
    resultado = numero + (numero * porcentaje // 100)
elif operacion == "-":
    resultado = numero - (numero * porcentaje // 100)
else:
    resultado = numero  # No cambia si la operación no es válida

# Mostrar resultado
print(f"Resultado final: {resultado}")