
rondas=int(input("Ingrese el número de rondas entre 3 y 6: "))
while rondas<3 or rondas>6:
    print("Debe ser un numero entre 3 y 6.")
    rondas=int(input("Ingrese el número de rondas entre 3 y 6: "))
for i in range(rondas):
    print("Ronda", i+1)


nnatural=int(input("Ingrese un número natural, el cual se hara la suma desde 1: "))
for n in range(1, nnatural+1):
    print(n)
suma=nnatural*(nnatural+1)//2

resultado_c=int(input("Ingrese el calculo que ud hizo: "))
print("La suma de los números naturales desde 1 hasta", nnatural, "es:", suma)
if resultado_c==suma:
    print("El resultado es Correcto ud gano 10 puntos")
else:    print("El resultado correcto es incorrecto")
