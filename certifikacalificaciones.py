calificacion = float(input("Ingrese la calificación del alumno: "))

if calificacion > 6.0:
    print("El alumno recibe un descuento del 20%")
elif calificacion > 5.0:
    print("El alumno recibe un descuento del 15%")
elif calificacion >= 4.0:
    print("El alumno recibe un descuento del 10%")
else:
    print("Invitamos al alumno a esforzarse para cumplir los requisitos.")