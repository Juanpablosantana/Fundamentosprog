# menu

#opciones

#1.saludo

#2.despedida

#3.edad

#4.opcion invalida

# dato clave utiliza if - elif- else



print("Menú de opciones:")

print("1. Saludo")

print("2. Despedida")

print("3. Edad")

print("4. Opción inválida")



opcion = int(input("Seleccione una opción (1-4): "))



if opcion == 1:

  print("¡Hola! ¿Cómo estás?")

elif opcion == 2:

  print(" Que tengas un buen día.")

elif opcion == 3:

  Fecha_nacimiento = int(input("Ingresa tu año de nacimiento: "))

  edad = 2025 - Fecha_nacimiento

  print(f"Tienes aproximadamente {edad} años.")

else:

  print("Opción inválida, por favor selecciona un número entre 1 y 3.")