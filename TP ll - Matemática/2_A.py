FR = {3,6,8,9,4,3,3,3}
CR = {3,9,9,5,9,3,7,1}
NI = {3,0,8,6,0,3,1,7}
GO = {3,2,7,1,4,2,3,6}
IV = {3,7,7,8,6,4,9,3}

dnis = [
        [3,6,8,9,4,3,3,3],  
        [3,9,9,5,9,3,7,1],
        [3,0,8,6,0,3,1,7],
        [3,2,7,1,4,2,3,6],
        [3,7,7,8,6,4,9,3]
        ]

#Si todos los conjuntos tienen al menos 5 elementos, entonces se considera que hay una alta diversidad numérica.·         
contador = 0
for i in range(len(dnis)):
    if len(dnis[i]) >= 5:
        contador += 1
if contador >= 5:
    print(f"Alta diversidad numérica")
else:
    print(f"No hay una alta diversidad numérica")

#Definiremos si hay más elementos pares que impares o viceversa.
par = 0
impar = 0

for dni in dnis:
    for n in dni:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1     

if par > impar:
    print("Hay mas registros PARES.")
elif impar > par:
    print("Hay mas IMPARES")
else:
    print("La cantidad de registros pares e impares son iguales")

