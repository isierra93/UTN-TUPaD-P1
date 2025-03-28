"""Actividades"""
"""1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""

print("Hola Mundo!")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla."""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su paiís de origen: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro"""

radio = float(input("Ingrese el radio de un círculo: "))
area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio
print(f"El área es {area} y su perímetro es {perimetro}.")

""" 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""

segundos = int(input("Ingrese una cantidad de segundos: "))
en_horas = (segundos / 60) / 60
print(f"{segundos} son {en_horas} hs.")

""" 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número. """

numero = int(input("Ingrese un número: "))
print(f"{numero*1}, {numero*2}, {numero*3}, {numero*4}, {numero*5}, {numero*6}, {numero*7}, {numero*8}, {numero*9}, {numero*10}")

""" 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

numero1 = int(input("Ingrese un número distinto de 0: "))
numero2 = int(input("Ingrese otro número distinto de 0: "))
if numero1 == 0 or numero2 == 0:
    print("Ambos numeros deben ser distintos de 0.")
else:
    print(f"La suma de los números: {numero1 + numero2}")
    print(f"La division de los números: {numero1 / numero2}")
    print(f"La multiplicación de los números: {numero1 * numero2}")
    print(f"La resta de los números: {numero1 - numero2}")

""" 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo: IMC = PESO EN KG / ALTURA EN M**2 """

peso = float(input("Ingrese su peso en kg : "))
altura = float(input("Ingrese su altura en m : "))
imc = peso / (altura**2)

print(f"Su índice de masa corporal es {imc}")

""" 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: """

celsius_temp = float(input("Ingrese la temperatura en C°: "))
fahrenheit_temp = (celsius_temp * 9 / 5) + 32
print(f"La temperatura en Fahrenheit es : {fahrenheit_temp}")

""" 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es : {promedio}")