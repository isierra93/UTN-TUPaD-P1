import time
import random

# Algoritmo de búsqueda lineal (O(n))
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

# Algoritmo de búsqueda binaria (O(log n))
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Generar lista ordenada
n = 100_000
lista = sorted(random.sample(range(n * 2), n))  # Sin repetidos
objetivo = lista[-1]  # Elegimos el último número para forzar el peor caso

# Medir tiempos
inicio = time.time()
resultado_lineal = busqueda_lineal(lista, objetivo)
tiempo_lineal = time.time() - inicio

inicio = time.time()
resultado_binaria = busqueda_binaria(lista, objetivo)
tiempo_binaria = time.time() - inicio

# Resultados
print(f"Búsqueda lineal: índice {resultado_lineal}, tiempo: {tiempo_lineal:.6f} seg")
print(f"Búsqueda binaria: índice {resultado_binaria}, tiempo: {tiempo_binaria:.6f} seg")

