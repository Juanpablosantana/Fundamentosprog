print("Bivenido a las fondas de los programadores mas basados del DUOC")
print("A continuacion nuestro menú de productos")
print("********************************************")
print("1.-Empanada de pino $2000")
print("2.-Empanada de queso $1500")
print("3.-Choripan $2500")
print("4.-Terremoto $1000")

cantidad_productos=0
total=0

while True:
    try:
        print("Por favor, si no desea un producto, ingrese 0")
        empanada_pino=int(input("Ingrese la cantidad de E. pino que desea: "))
        empanada_queso=int(input("Ingrese la cantidad de E. queso que desea: "))
        choripan=int(input("Ingrese la cantidad de choripan que desea: "))
        terremoto=int(input("Ingrese la cantidad de terremoto que desea: "))
        if empanada_pino >=0 and empanada_queso>=0 and choripan>=0 and terremoto>=0:
            print("Compra ingresada con exito")
            break
        else:
            print("Ingrese un numero positivo")
            continue
    except ValueError:
        print("Ingrese un caracter valido")
        continue

cantidad_productos+=empanada_pino+empanada_queso+choripan+terremoto
total += empanada_pino * 2000
total += empanada_queso * 1500
total += choripan * 2500
total += terremoto * 1000

if total >20000:
    descuento=total*0.40
    total_descuento=total - descuento
    print("Por tu compra, recibiste un descuento del 40%")
elif total > 10000:
    descuento=total*0.25
    total_descuento=total-descuento
    print("Por tu compra recibiste un descuento del 25%")
else:
    print("Gracias por tu compra. No recibió descuento")

print(f"Tu cantidad de productos fue {cantidad_productos}")
print(f"Tu total a pagar sin descuento es de {total}")
print(f"Tu total a pagar con descuento es {total_descuento}")