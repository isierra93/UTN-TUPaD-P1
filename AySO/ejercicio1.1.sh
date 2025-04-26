#Ejercicio 1.1: Crear un script en Bash que muestre el valor de seis variables de entorno del sistema. 
#: 1. El script debe mostrar el valor de las siguientes variables de entorno: 
# o LOGNAME: El nombre del usuario con el que se ha iniciado sesión. 
# o HOME: El directorio home del usuario. 
# o SHELL: El shell predeterminado del usuario. 
# o PWD: El directorio de trabajo actual. 
# o USER: El nombre de usuario del que se ha iniciado sesión. 
# o SSH_TTY: El terminal asociado a la sesión SSH, si está disponible. 
# 2. El script debe mostrar el valor de cada una de estas variables de entorno de forma clara y enunciativa, 
# por ejemplo: o "La variable LOGNAME tiene el valor XXX" o "La variable HOME tiene el valor YYY" 
# 3. Pasos adicionales: o El script puede comenzar limpiando la pantalla para una mejor presentación, aunque esto es opcional. 


#!/bin/bash
clear 

echo "El nombre de usuario con el que se ha iniciado sesión (LOGNAME): $LOGNAME"
echo "El directorio home del usuario (HOME): $HOME"
echo "El shell predeterminado del usuario (SHELL): $SHELL"
echo "El directorio de trabajo actual (PWD): $PWD"
echo "El nombre de usuario del que se ha iniciado sesión (USER): $USER"
echo "El terminal asociado a la sesión SSH (SSH_TTY): $SSH_TTY"