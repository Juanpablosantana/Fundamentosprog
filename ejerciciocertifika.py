# Certifica
# Realizar un programa con las siguientes condiciones:
# Alumnos con calificaciones mayor a 6.0 recibiran un descuento de 20%
# Alumnos con calificaciones mayor a 5.0 recibiran un descuento de 15%
# Alumnos con calificaciones mayor a 4.0 recibiran un descuento de 10%
# El Que no cumpla con estos requisitos lo invitamos a esforzarse para cumplir

def calcular_descuento(calificacion):
    if calificacion > 6.0:
        return 20
    elif calificacion > 5.0:
        return 15
    elif calificacion > 4.0:
        return 10
    else:
        return 0

# Mensaje de bienvenida
print("¡Bienvenido al sistema de cálculo de descuentos para alumnos!")
print("Ingrese la calificación para conocer el descuento aplicado.\n")

# Solicitar la calificación al usuario
calificacion = float(input("Ingrese la calificación del alumno: "))
descuento = calcular_descuento(calificacion)

if descuento > 0:
    print(f"El alumno recibe un descuento del {descuento}%.")
else:
    print("El alumno no cumple con los requisitos de descuento. ¡Sigue esforzándote!")

