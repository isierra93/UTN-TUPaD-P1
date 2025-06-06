import time

inicio = time.time()
resultado = sum(range(1000000))
fin = time.time()

print("Tiempo de ejecución:", fin - inicio, "segundos")