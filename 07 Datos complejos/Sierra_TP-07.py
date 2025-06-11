"""Actividades
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""

lista_sin_precios = list(precios_frutas.keys())

"""4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
mensaje de saludo que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
años.
"""

class Persona:
    def __init__(self, nombre:str, pais:str , edad:int) -> None:
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        return f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años."
    
francisco = Persona("Jorge Mario Bergoglio", "Argentina", 88)

"""5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
"""

from math import pi

class Circulo:
    def __init__(self, radio:float) -> None:
        self.radio = radio

    def calcular_area(self):
        return round(pi * self.radio ** 2, 3)

    def calcular_perimetro(self):
        return round(self.radio * 2 * pi , 3)

jabulani = Circulo(0.11)
print(jabulani.calcular_area())
print(jabulani.calcular_perimetro())

"""6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
balanceados usando una pila.
# balanceado(([{}])) -> True
# balanceado(([{])) -> False
"""

from collections import deque

class Pila:
    def __init__(self, claves:dict = { "(":")", "[":"]", "{":"}" }) -> None:
        self.elementos = deque()
        self.claves = claves
    
    def esta_vacia(self):
        return len(self.elementos) == 0  
    
    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else "La pila está vacía"
 
    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else "La pila está vacía"
    
def balanceado(cadena:str) -> bool:
    es_balanceado:bool = False

    pila = Pila()

    for e in cadena:
        if e in pila.claves.keys():
            pila.apilar(e)
        elif e in pila.claves.values():
            if pila.esta_vacia() or pila.claves[pila.ver_tope()] != e:
                return False
            pila.desapilar()

    if pila.esta_vacia():
        es_balanceado = True
    
    return es_balanceado

print(balanceado("([)])"))

"""7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila.
"""

class Cola:
    def __init__(self) -> None:
        self.elementos = deque()

    def agregar_cliente(self, elemento):
        self.elementos.append(elemento)

    def atender_cliente(self):
        self.elementos.popleft()

    def mostrar_siguiente_cliente(self):
        return self.elementos[0] if self.elementos else "La lista esta vacia"


""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
 """

productos_8 = {"arroz" : 10, "leche" : 3, "yerba" : 100}
print(productos_8)
print(f"Stock de arroz: {productos_8["arroz"]} .")
productos_8["arroz"] += 1
productos_8["pan"] = 5
print(productos_8)

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
 """

agenda = {
    ("Lunes", "9 AM") : "Asistir al medico",
    ("Miercoles", "7 PM") : "Partido de futbol",
    ("Sabado", "2 PM") : "Asado en Pilar"
}

print(agenda[("Miercoles", "7 PM")])

""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores. """

paises_original:dict = {
    "Argentina" : "Buenos Aires",
    "Chile" : "Santiago de Chile",
    "USA" : "Washington DC"
}
print("Original", paises_original)

paises_copia_inversa:dict = {}

for pais in paises_original:
    paises_copia_inversa[paises_original[pais]] = pais

print("Copia inversa" , paises_copia_inversa)