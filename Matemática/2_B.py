""" B. Operaciones con años de nacimiento

·         Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).

·         Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.

·         Si todos nacieron después del 2000, mostrar "Grupo Z".

·         Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".

·         Implementar una función para determinar si un año es bisiesto.

·         Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.
 """
from datetime import date
anio_actual = date.today().year

#Inicialización de variables
anios_pares = 0
anios_impares = 0
gen_z = True
anio_biciesto = False
CA = set()
CE = set()
CAXCE = set()

#Solicitar años
for i in range(5):
    n = int(input("Ingrese el año de nacimiento: "))
    CA.add(n)
    CE.add(anio_actual-n)

print("CONJUNTO AÑOS:", CA)
print("CONJUNTO EDADES:", CE)

#Funcion para verificar si es biciesto
def is_biciesto(anio):
    if anio % 4 == 0 or anio % 100 == 0 and anio % 400 != 0:
        return True
    return False
#Verificar años pares
for anio in CA:
    #Verifica y cuenta años pares/impares
    if anio % 2 == 0:
        anios_pares = anios_pares + 1
    else:
        anios_impares = anios_impares + 1
    #Verifica si es Grupo Z
    if anio < 2000:
        gen_z = False
    #Verificar anio biciesto
    if anio_biciesto == False:
        anio_biciesto = is_biciesto(anio)
    #Calcular producto cartesiano entre conjunto años y conjunto edades actuales CA X CE
    #Cada año, juntarlo con cada edad
    for edad in CE:
        CAXCE.add((anio,edad))


print(f"Nacidos en años pares: {anios_pares} y en años impares {anios_impares}.")
if gen_z:
    print("Grupo Z")
if anio_biciesto:
    print("Tenemos un año especial") 
print(f"El producto cartesiano entre el conjunto de años y el conjunto de edades actuales es: {CAXCE}")