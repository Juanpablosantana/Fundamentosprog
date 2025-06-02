# ==========================================
# CLASE PREPARADA – EVALUACIÓN PARCIAL 3
# Asignatura: Fundamentos de Programación
# Unidad: EA2 – Programación de aplicaciones en Python
# ==========================================

#  OBJETIVOS:
# - Comprender ciclos, condicionales y excepciones.
# - Usar while, if-else y try-except.
# - Practicar con ejercicios similares a la evaluación parcial.

# ==========================================
# ¿QUÉ ES UN WHILE?
# ==========================================
"""
El while es una estructura de repetición que ejecuta un bloque de código mientras una condición sea verdadera.
"""

# Ejemplo simple:
contador = 1
while contador <= 3:
    print("Hola", contador)
    contador += 1

# Ejemplo práctico con validación:
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except:
        print("¡Eso no es un número! Intenta de nuevo.")

# ==========================================
# ¿QUÉ ES IF - ELSE?
# ==========================================
"""
Estructura condicional que se usa para tomar decisiones.
"""

edad = 10
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

nota = 9
if nota >= 9:
    print("¡Excelente!")
elif nota >= 6:
    print("Muy bien")
else:
    print("Necesitas mejorar")

numero = int(input("Escribe un número entre 0 y 100: "))
if 0 <= numero <= 100:
    print("Número válido")
else:
    print("Número fuera de rango")

# ==========================================
# ¿QUÉ ES TRY - EXCEPT?
# ==========================================
"""
Estructura para manejar errores. Intenta algo, y si falla, captura el error.
"""

try:
    edad = int(input("¿Cuántos años tienes? "))
    print("Tienes", edad, "años")
except:
    print("Eso no es un número válido")

# Ejemplo con ciclo para validar número:
while True:
    try:
        numero = int(input("Ingresa un número entre 0 y 100: "))
        break
    except:
        print("¡Eso no es un número entero! Intenta de nuevo.")

# ==========================================
# EJERCICIO MODELO 1 – VACUNACIÓN
# ==========================================
"""
Registra N personas y verifica si tienen el esquema completo de vacunación (3 dosis).
"""

while True:
    try:
        cant = int(input("Ingrese la cantidad de personas a registrar: "))
        break
    except:
        print("Debe ingresar un número entero.")

completos = 0
incompletos = 0

for _ in range(cant):
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas: "))
            break
        except:
            print("Debe ingresar un número entero.")

    if dosis >= 3:
        print("Esquema completo.")
        completos += 1
    else:
        print("Esquema incompleto.")
        incompletos += 1

print(f"Se registraron {completos} personas con esquema completo.")
print(f"Se registraron {incompletos} personas con esquema incompleto.")

# ==========================================
# EJERCICIO MODELO 2 – MENÚ CON OPCIONES
# ==========================================
mayor = -1
suma = 0
contador = 0

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar promedio.")
    print("4. Terminar programa.")

    opcion = input("Elija opción: ")

    if opcion == "1":
        while True:
            try:
                n = int(input("Ingrese número entre 0 y 100: "))
                if 0 <= n <= 100:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100!!")
            except:
                print("Debe ingresar un número entero!!")

        if n > mayor:
            mayor = n
        suma += n
        contador += 1

    elif opcion == "2":
        if contador == 0:
            print("No se han ingresado números.")
        else:
            print("El número mayor hasta el momento es:", mayor)

    elif opcion == "3":
        if contador == 0:
            print("No se han ingresado números para calcular el promedio.")
        else:
            promedio = suma / contador
            print(f"El promedio de los números ingresados es: {promedio:.2f}")

    elif opcion == "4":
        print("Fin del programa. Adiós.")
        break

    else:
        print("Debe ingresar una opción válida.")

# ==========================================
# 📝 TAREA PROPUESTA
# ==========================================
"""
- Opción 5: Mostrar cuántos números se han ingresado.
- Opción 6: Borrar todos los números (reiniciar).
- Mantener validaciones con try-except.
"""
