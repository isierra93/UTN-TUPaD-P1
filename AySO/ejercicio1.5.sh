# Ejercicio 1.5: Crear un script que realice las cuatro operaciones básicas (suma, resta,
# multiplicación, división) con dos números proporcionados como parámetros. El script debe
# comprobar la cantidad de parámetros y realizar diferentes acciones según el número de
# parámetros ingresados, mostrando mensajes adecuados en cada caso

#!/bin/bash

clear

# Función para realizar las operaciones básicas
realizar_operaciones() {
    num1=$1
    num2=$2

    # Mostrar los resultados de las operaciones básicas
    echo "Suma: $((num1 + num2))"
    echo "Resta: $((num1 - num2))"
    echo "Multiplicación: $((num1 * num2))"

    if [ "$num2" -eq 0 ]; then
        echo "División: Error - No se puede dividir entre cero."
    else
        echo "División: $((num1 / num2))"
    fi
}

# Verificar la cantidad de parámetros
if [ "$#" -eq 0 ]; then
    echo "No ha introducido ninguno. ¿Quiere ahora s/n?"
    read decision
    if [[ "$decision" == "s" || "$decision" == "S" ]]; then
        echo "Por favor, ingrese el primer número:"
        read num1
        echo "Por favor, ingrese el segundo número:"
        read num2
        realizar_operaciones "$num1" "$num2"
    fi
elif [ "$#" -eq 1 ]; then
    echo "Ha introducido uno. ¿Quiere ahora s/n?"
    read decision
    if [[ "$decision" == "s" || "$decision" == "S" ]]; then
        num1="$1"
        echo "Por favor, ingrese el segundo número:"
        read num2
        realizar_operaciones "$num1" "$num2"
    fi
elif [ "$#" -gt 2 ]; then
    echo "Demasiados parámetros, tomo los dos primeros."
    num1="$1"
    num2="$2"
    realizar_operaciones "$num1" "$num2"
else # Equivalente a [ "$#" -eq 2 ]
    echo "CORRECTO"
    num1="$1"
    num2="$2"
    realizar_operaciones "$num1" "$num2"
fi



