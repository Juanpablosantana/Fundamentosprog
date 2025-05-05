a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
def Operacion(a, b):
    return a + b, a * b, a - b, a / b
resultado = Operacion(a, b)
print("Resultado", resultado)


