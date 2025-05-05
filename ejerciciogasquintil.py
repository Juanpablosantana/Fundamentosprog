#calcular subsidio de gas
def calcular_subsidio_de_gas (Quintil, Condicion_Lab, Subsidio_gas, Edad):
    if Quintil == 1 and Condicion_Lab == "Desempleado":
        Subsidio_gas = 15000
    elif Quintil == 2 and Condicion_Lab == "Empleado":
        Subsidio_gas = 10000
    elif Quintil == 3 and Condicion_Lab == "Desempleado":
        Subsidio_gas = 8000
    elif Quintil == 4 and Condicion_Lab == "Empleado":
        Subsidio_gas = 6000
    elif Quintil == 5 and Condicion_Lab == "Cualquiera":
        Subsidio_gas = 1500
    else:
        Subsidio_gas = 0 

    # bonos adicionales
    if Quintil in [1, 2]:
        Subsidio_gas += 2000
    if Edad >= 65 :
        Subsidio_gas += 3000  
    return Subsidio_gas        

#pedir datos al usuario
quintil = int(input("Ingrese su quintil (1-5): "))
condicion_lab = input("Ingrese su condicion laboral (Empleado/Desempleado/Cualquiera): ")
edad = int(input("Ingrese su edad: "))

# CALCULAR  SUBSIDIO TOTAL
Subsidio_Total = calcular_subsidio_de_gas(quintil, condicion_lab, 0, edad)
print("El subsidio total es: ", Subsidio_Total)