import matplotlib.pyplot as plt
import numpy as np
import math

# Rango de entrada
n = np.linspace(1, 10, 100)

# Definición de funciones de complejidad
O_1 = np.ones_like(n)
O_log_n = np.log2(n)
O_n = n
O_n_log_n = n * np.log2(n)
O_n2 = n ** 2
O_n3 = n ** 3
O_2n = 2 ** n
O_fact_n = [math.factorial(int(i)) if i <= 10 else np.nan for i in n]  # Evitamos overflow

# Crear el gráfico
plt.figure(figsize=(12, 8))
plt.plot(n, O_1, label="O(1)")
plt.plot(n, O_log_n, label="O(log n)")
plt.plot(n, O_n, label="O(n)")
plt.plot(n, O_n_log_n, label="O(n log n)")
plt.plot(n, O_n2, label="O(n²)")
plt.plot(n, O_n3, label="O(n³)")
plt.plot(n, O_2n, label="O(2ⁿ)")
plt.plot(n, O_fact_n, label="O(n!)")

# Ajustes estéticos
plt.ylim(0, 1000)  # Limitar eje Y para que todo sea visible
plt.title("Comparación de Complejidades (Notación Big O)")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Crecimiento estimado")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar gráfico
plt.show()
