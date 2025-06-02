def registrar_libros():
    cantidad = int(input("¿Cuántos libros quieres registrar? "))
    i = 0
    
    while i < cantidad:
        titulo = input("Título del libro: ")
        print(f"Libro '{titulo}' registrado.")
        i += 1

registrar_libros()