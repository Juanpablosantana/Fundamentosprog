productos = {
    "Perfume Organza Girl": 10000,
    "Perfume Katy Perry": 10000,
    "Mañana Fresca Girl": 10000,
    "Perfume La Mejor Noche Girl": 10000,
    "Perfume Sueño Exclusivo Girl": 10000,
    "Perfume Ahora Sí Voy": 10000,
    "Perfume Antonio Bandera": 10000,
    "Perfume Lacoste": 10000,
    "Perfume Hugo Boss": 10000,
    "Perfume A Que Te Quito el Sueño": 10000
}

iva = 0.19
carrito = []

print("Lista de productos disponibles:")
for i, producto in enumerate(productos, 1):
    print(f"{i}. {producto} - ${productos[producto]:.2f}")

while True:
    seleccion = input("\nIngresa el número del producto que deseas agregar (o '0' para terminar): ")
    if seleccion == "0":
        break
    elif seleccion.isdigit() and 1 <= int(seleccion) <= len(productos):
        producto_elegido = list(productos.keys())[int(seleccion) - 1]
        carrito.append(producto_elegido)
        print(f"✅ {producto_elegido} agregado al carrito.")
    else:
        print("❌ Opción inválida. Intenta nuevamente.")

subtotal = sum(productos[p] for p in carrito)
impuestos = subtotal * iva
total = subtotal + impuestos

print("\nResumen del carrito:")
for p in carrito:
    print(f"- {p}: ${productos[p]:.2f}")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"IVA ({iva * 100}%): ${impuestos:.2f}")
print(f"Total a pagar: ${total:.2f}")