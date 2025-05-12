# Los Dueños del vivero San Joaquín necesitan realizar un programa en python.
# Inventaio y Ventas de las plantas.
# Productos:
# 1. Rosa Blanca (excelente para esta primavera $2000)
# 2. La Mata de Navidad (importada desde mexico para recordar la navidad $5000)
# 3. La orquidea (la flor más hermosa del mundo $3000)
# 4. Copihue (el árbol nacional de Chile $10000)
# 5. Rosas Rojas (Una excelente eleccion para el dia de los enamorados $7000)
# Generar un archivo txt, que almanece tus primeras 5 plantas en tu inventario y que pueda quedar abierto para agregar más plantas.

with open('Inventario_Plantas.txt', 'w') as archivo:
    # Definir los productos con su información
    productos = [
        ("Rosa Blanca", "Excelente para esta primavera", 2000),
        ("Mata de Navidad", "Importada desde México para recordar la navidad", 5000),
        ("Orquidea", "La flor mas hermosa del mundo", 3000),
        ("Copihue", "El arbol nacional de Chile", 10000),
        ("Rosas Rojas", "Una excelente eleccion para el dia de los enamorados", 7000)
        

    ]

    # Escribir los productos en el archivo
    for i, (nombre, descripcion, precio) in enumerate(productos, start=1):
        archivo.write(f"{i}. Tipo: {nombre}\n")
        archivo.write(f"Descripción: {descripcion}\n")
        archivo.write(f"Precio: ${precio}\n\n")
print("Inventario guardado correctamente.")