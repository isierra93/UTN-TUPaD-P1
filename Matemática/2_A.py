''' A. Operaciones con DNIs
·         Ingreso de los DNIs (reales o ficticios). ✅
·         Generación automática de los conjuntos de dígitos únicos. ✅
·         Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
·         Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
·         Suma total de los dígitos de cada DNI.
·         Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
Ejemplos:
·         Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".
·         Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta". ✅''' 


dnis_conjunto = set()


#Solicito x numeros de DNI y los agrego al listado de DNIS
for i in range(2):
    n = input("Ingrese un numero de DNI: ")
    digitos_unicos = set(n)
    dnis_conjunto.add(tuple(digitos_unicos))
print("Conjunto de DNIs:", dnis_conjunto)

diversidad_numerica = False
conjunto_union = set()
conjunto_interseccion = set()
for conjunto in dnis_conjunto:
    conjunto_union = conjunto_union.union(conjunto)
    conjunto_interseccion = conjunto.intesection(conjunto_interseccion)
    if len(conjunto) > 6:
        diversidad_numerica = True
print("Union de conjuntos:", conjunto_union)
print("Interseccion de conjuntos:", conjunto_interseccion)
if diversidad_numerica:
    print("Diversidad numerica alta.")


