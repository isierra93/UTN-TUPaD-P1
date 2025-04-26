# Ejercicio 1.2: Crear un script en Bash que pida un nombre de usuario y un mensaje, y luego envíe ese mensaje al usuario especificado utilizando el comando write. Requisitos: 
# 1. El script debe pedir al usuario que ingrese un nombre de usuario. 
# 2. Luego debe solicitar un mensaje que el script enviará al usuario indicado previamente. 
# 3. El script debe enviar el mensaje al usuario especificado utilizando el comando write. 

#!/bin/bash
clear 

read -p "Ingrese el nombre de usuario al que desea enviar el mensaje: " destino
read -p "Ingrese el mensaje que desea enviar a $destino: " mensaje
echo "$mensaje" > mensaje.txt
cat mensaje.txt | write "$destino"