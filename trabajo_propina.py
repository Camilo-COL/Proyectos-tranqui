cuenta=int(input("Ingrese el total de la cuenta: "))
propina=int(input("Ingrese la propina: "))

calculo=propina/100
total_propina=cuenta*calculo 
total_pagar=cuenta+total_propina

print("El total de la propina es: ", total_propina)
print("El total a pagar es: ", total_pagar)
