#construye un sistema simple de venta para una fonda
# productos disponibles:
# 1. Empanadas: $3000
# 2. Empanadas de queso: $2500
# 3. Choripanes: $2000
# 4. Terremotos: $1000
# El usuario puede seleccionar un producto y una cantidad
# El sistema calcula el total de la compra
# por compras mayor a $10000, se aplica un descuento del 10%
# y por compras mayor a $20000, se aplica un descuento del 40%
# por compras mayor a las otras 2 opciones, las entradas son gratis

while True:
    try:
       pino = int(input("Empanadas de pino: ")) * 2000
       queso = int(input("Empanadas de queso: ")) * 1500
       choripan = int(input("Choripanes: ")) * 2500
       terremoto = int(input("Terremotos: ")) * 1000

    total = pino + queso + choripan + terremoto

    if total > 20000:
         print(f"Total: {total} - Descuento 40%. Entradas gratis.")
    elif total > 10000:
        print(f"Total con descuento 25%: {total * 0.75}")
else:
print(f"Total a pagar: {total}")