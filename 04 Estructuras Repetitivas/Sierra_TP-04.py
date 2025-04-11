"""
Actividades
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""

for i in range(101):
    print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

contador_digitos = 0
numero = int(input("Ingrese un numero: "))

if numero == 0:
  contador_digitos += 1
elif numero < 0:
  numero = abs(numero)

while numero > 0:
  contador_digitos += 1

  numero //= 10

print(f"El numero ingresado posee {contador_digitos} digitos.")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese otro numero: "))
resultado = 0

if primer_numero != segundo_numero:
    if primer_numero > segundo_numero:
        numero_max = primer_numero
        numero_min = segundo_numero
    else:
        numero_max = segundo_numero
        numero_min = primer_numero

    for i in range(numero_min+1, numero_max):
        resultado += i
    print(f"La suma es: {resultado}")

else:
    print("Los numeros son iguales.")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

sumaTotal = 0
numero = int(input("Ingrese un numero: "))

while numero != 0:
  sumaTotal += numero
  numero = int(input("Ingrese un numero: "))

print(f"La suma total es: {sumaTotal}")

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
from random import randint

numero_aleatorio = randint(0,9)
contador_intentos = 1

numero = int(input("Ingrese un numero: "))

while numero != numero_aleatorio:
  contador_intentos += 1
  print("Numero incorrecto.")
  numero = int(input("Ingrese un numero: "))

print(f"Correcto!, El numero era: {numero_aleatorio} y necesitaste {contador_intentos} intentos.")

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
for i in range(100,-1, -1):
  if i % 2 == 0:
    print(i)

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
numero = int(input("Ingrese un numero: "))
suma_total = 0

if numero > 0:
  for i in range(numero+1):
    suma_total += i
  print(f"La suma total es {suma_total}")
else:
  print("EL numero debe ser positivo.")

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
NUMEROS_TOTALES = 100

cont_pares = 0
cont_impares = 0

cont_negativos = 0
cont_positivos = 0

for i in range(NUMEROS_TOTALES):
  numero = int(input("Ingrese un numero: "))
  if numero % 2 == 0:
    cont_pares += 1
  else:
    cont_impares += 1
  
  if numero > 0:
    cont_positivos += 1
  else:
    cont_negativos += 1

print("Numeros positivos:", cont_positivos)
print("Numeros negativos:", cont_negativos)
print("Numeros pares:", cont_pares)
print("Numeros impares:", cont_impares)

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
TOTAL_NUMEROS = 100
suma_total_numeros = 0
media_valores = 0

for i in range(TOTAL_NUMEROS):
  ingreso = int(input("Ingrese un numero: "))
  suma_total_numeros += ingreso

media_valores = suma_total_numeros / TOTAL_NUMEROS
print("La media es", media_valores)

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingrese un numero: "))

numero_invertido = 0

while numero > 0:
  digito = numero % 10
  numero_invertido = numero_invertido * 10 + digito

  numero = numero // 10

print(f"El numero invertido es: {numero_invertido}.")