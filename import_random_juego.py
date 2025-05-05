import random

min_val = int(input("Mínimo: "))
max_val = int(input("Máximo: "))

if min_val < max_val:
    numero = round(random.randint(min_val, max_val) / 4) * 4

    for _ in range(3):
        if int(input("Adivina: ")) == numero:
            print("¡Ganaste!")
            break
    else:
        print(f"Perdiste, el número era {numero}.")
else:
    print("El mínimo debe ser menor que el máximo.")