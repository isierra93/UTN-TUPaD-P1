# Ejercicio 1.4: Crear un script en Bash que pida al usuario dos cadenas de texto, verifique si
# alguna de ellas está vacía y, finalmente, compare ambas cadenas para determinar si son
# iguales o no. 

#!/bin/bash

clear

# Solicitar al usuario la primera cadena de texto
echo "Por favor, ingrese la primera cadena de texto:"
read cadena1

# Solicitar al usuario la segunda cadena de texto
echo "Por favor, ingrese la segunda cadena de texto:"
read cadena2

# Verificar si la primera cadena está vacía
if [ -z "$cadena1" ]; then
    echo "La cadena1 está vacía."
else
    echo "La cadena1 no está vacía."
fi

# Verificar si la segunda cadena está vacía
if [ -z "$cadena2" ]; then
    echo "La cadena2 está vacía."
else
    echo "La cadena2 no está vacía."
fi

# Comparar ambas cadenas para determinar si son iguales o diferentes
if [ "$cadena1" == "$cadena2" ]; then
    echo "Las cadenas son iguales."
else
    echo "Las cadenas son diferentes."
fi