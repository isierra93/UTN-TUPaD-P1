"""
Actividades:
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""

def imprimir_hola_mundo(mensaje):
    print(mensaje)

imprimir_hola_mundo("Hola Mundo!")

"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
nombre = input("Ingrese su nombre: ")
def saludar_usuario(nombre:str):
    print(f"Hola {nombre.capitalize()} !")

saludar_usuario(nombre)

"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal(nombre:str, apellido:str, edad:int, residencia:str) -> None:
  print(f"Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""

import math

def calcular_area_circulo(r:float) -> float:
  return math.pi * r ** 2

def calcular_perimetro_circulo(r:float) -> float:
  return 2 * r * math.pi

radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {round(area, 2)} y el perimetro es {round(perimetro, 2)}.")

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""

def segundos_a_horas(segundos:int):
  return round((segundos / 60) / 60, 2)

segs = int(input("Ingrese los segundos a convertir en horas: "))
horas = segundos_a_horas(segs)

print(f"{segs} segundos es igual a {horas} horas.")

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

def tabla_multiplicar(numero:int) -> None:
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")

numero = int(input("Ingrese un numero para imprimir la tabla: "))
tabla_multiplicar(numero)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
"""

def operaciones_basicas(a, b) -> tuple:
  suma = a + b
  resta = a - b
  mult = a * b
  div = a / b
  return (suma, resta, mult, div)

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un numero:"))

result = operaciones_basicas(num1, num2)

print(f"La suma: {result[0]}")
print(f"La resta: {result[1]}")
print(f"La multiplicación: {result[2]}")
print(f"La división: {result[3]}")

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""

def calcular_imc(peso:float, altura:float) -> float:
  #IMC = peso (kg)/ [estatura (m)]2
  imc = peso / altura**2
  return imc

peso_en_kg = float(input("Ingrese su peso en KG: "))
altura_en_metros = float(input("Ingrese su altura en Metros: "))
imc = round(calcular_imc(peso_en_kg, altura_en_metros), 2)

print(f"Su indice de masa corporal es de: {imc}")

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""

def celsius_a_fahrenheit(celsius:float) -> float:
  #Para convertir Celsius a Fahrenheit: °F = (°C * 9/5) + 32
  return (celsius*9/5) + 32

grados = float(input("Ingrese la temperatura en C°: "))
grados_en_celsius = celsius_a_fahrenheit(grados)

print(f"El equivalente de {grados} C° es de {grados_en_celsius} F°")

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""

def calcular_promedio(a, b, c) -> float:
  return (a+b+c) / 3

def solicitar_y_asignar():
  num = float(input("Ingrese un numero: "))
  while num < 0 or num > 10:
    num = float(input("ERROR. Ingrese un numero: "))
  return num

num1 = solicitar_y_asignar()
num2 = solicitar_y_asignar()
num3 = solicitar_y_asignar()

print(f"El promedio es: {round(calcular_promedio(num1,num2,num3), 2)}")