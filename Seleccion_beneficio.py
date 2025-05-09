valor_arancel = 1800000
valor_matricula = 90000
   
promedio = float(input("Ingrese su promedio de notas:"))
quintil = float(input("Ingrese su quintil 1-4 :"))

if promedio > 6.0 :
        descuento_arancel = 0.20 if quintil <= 4 else 0.0
elif promedio >= 5.0 :
        descuento_arancel = 0.13 if quintil <= 4 else 0.0
else:
        descuento_arancel = 0.0    

descuento_matricula = 0.10 if quintil <= 3 else 0.0
if promedio >= 5.5 and quintil <= 3: 
        descuento_matricula += 0.05

valor_final_arancel = valor_arancel * (1 - descuento_arancel)
valor_final_matricula = valor_matricula * (1 - descuento_matricula)       

print("El arancel final", valor_final_arancel)
print("El valor final matricula", valor_final_matricula)