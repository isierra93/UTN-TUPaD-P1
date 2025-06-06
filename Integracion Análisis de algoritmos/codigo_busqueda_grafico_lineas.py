import time
import random
import matplotlib.pyplot as plt

# Algoritmos
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

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

# Rangos de tamaño de listas para comparar
tamaños = [1_000, 5_000, 10_000, 20_000, 50_000, 100_000]
tiempos_lineal = []
tiempos_binaria = []

# Medición de tiempos por tamaño
for n in tamaños:
    lista = sorted(random.sample(range(n * 2), n))
    objetivo = lista[-1]  # peor caso

    inicio = time.time()
    busqueda_lineal(lista, objetivo)
    tiempos_lineal.append(time.time() - inicio)

    inicio = time.time()
    busqueda_binaria(lista, objetivo)
    tiempos_binaria.append(time.time() - inicio)

# 📈 Gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(tamaños, tiempos_lineal, label='Búsqueda Lineal (O(n))', marker='o')
plt.plot(tamaños, tiempos_binaria, label='Búsqueda Binaria (O(log n))', marker='s')
plt.title('Comparación de Tiempo de Búsqueda vs Tamaño de Lista')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
