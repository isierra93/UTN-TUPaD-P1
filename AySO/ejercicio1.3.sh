# Ejercicio 1.3: Crear un script en Bash que reciba varios parámetros al ejecutarse y muestre un mensaje indicando el valor de cada uno de los parámetros. 
# Además, debe mostrar el número total de parámetros y el nombre del archivo del script

#!/bin/bash
clear

read -p "Ingrese el valor del parámetro 1: " parametro1
read -p "Ingrese el valor del parámetro 2: " parametro2
read -p "Ingrese el valor del parámetro 3: " parametro3
read -p "Ingrese el valor del parámetro 4: " parametro4
read -p "Ingrese el valor del parámetro 5: " parametro5
read -p "Ingrese el valor del parámetro 6: " parametro6
read -p "Ingrese el valor del parámetro 7: " parametro7
read -p "Ingrese el valor del parámetro 8: " parametro8
read -p "Ingrese el valor del parámetro 9: " parametro9

echo "El parámetro 1 es: $parametro1"
echo "El parámetro 2 es: $parametro2"
echo "El parámetro 3 es: $parametro3"
echo "El parámetro 4 es: $parametro4"
echo "El parámetro 5 es: $parametro5"
echo "El parámetro 6 es: $parametro6"
echo "El parámetro 7 es: $parametro7"
echo "El parámetro 8 es: $parametro8"
echo "El parámetro 9 es: $parametro9"

echo "El número total de parámetros ingresados es: 9"
echo "El número total de parámetros ingresados es: $# "
echo "Todos los parámetros juntos son:  $* "
echo "Todos los parámetros juntos son: $parametro1 $parametro2 $parametro3 $parametro4 $parametro5 $parametro6 $parametro7 $parametro8 $parametro9"
echo "El nombre del script es: $0"
