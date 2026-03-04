#codigo cajero 
saldo_actual=1000
print("1. ver saldo 2. retirar 3. depositar ")
op=int(input("Ingrese la opcion: "))
if op==1:
    print("Su saldo es: ", saldo_actual)
elif op==2:
    rt=int(input("Ingrese la cantidad a retirar: "))
    if rt<saldo_actual:
        calculo1=saldo_actual-rt
        print("su saldo ahora es de: ", calculo1)
    else:
        print("Fondos insuficientes.")
elif op==3:
    dp=int(input("Ingrese la cantidad a depositar: "))
    calculo2=saldo_actual+dp
    print("Su nuevo saldo es de: ", calculo2)
else:
    print("Opcion no valida, intente de nuevo.")