### MENU Y SISTEMA ###
def sistema(ltr):
    op_min = ltr.lower()
    if op_min == 'n':
        print('This is the end my friend :(')
    elif op_min == 'y':
        solicitar_dnis()
    else:
        ltr = input('La opcion seleccionada no existe. Por favor ingrese Y o N: ')
        sistema(ltr)

def solicitar_dnis():
    conjuntos = []
    n = 3 # Setea cantidad de DNIS a solicitar
    for i in range(1,n):
        dni_string = input(f'Debe ingresar {n-i} dnis. Por favor ingrese un dni valido sin puntos: ')
        array_dni_string = list(dni_string)
        array_dni_integers = list(map(int, array_dni_string))
        conjuntos.insert(i, array_dni_integers)
    print('#################################################################')
    for i in range(1,n):
        print(f'DNI_{conjuntos.index(conjuntos[i-1])} es igual a {conjuntos[i-1]}')
    print('#################################################################')
    elegir_operacion(conjuntos)   

def mostrar_dnis(array_1):
    print('#################################################################')
    for array in array_1:
        print(f'Conjunto numero {array_1.index(array)} es igual a {array}')
    print('#################################################################')
    elegir_operacion(array_1)

def continuacion(conjuntos):
    opcion = input('Desea continuar? (Y/N): ')
    op_min = opcion.lower()
    if (op_min != 'y' and op_min != 'n'):
        letr = input('La opcion seleccionada no existe. Por favor ingrese Y o N: ')
        if letr.lower() == 'n':
            print('This is the end my friend :(')    
        else: 
            elegir_operacion(conjuntos)
    elif op_min == 'n':
        print('This is the end my friend :(')
    else:
        elegir_operacion(conjuntos)
    
def elegir_operacion(conjuntos):    
    print(
        'OPERACIONES:\n' 
        'A. Numeros Unicos\n'
        'B. Union de Conjuntos\n'
        'C. Interseccion de Conjuntos\n'
        'D. Diferencia de conjuntos\n'
        'E. Diferencia simetrica de conjuntos\n'
        'F. Suma de numeros de un conjunto\n'
        'G. Resetear DNIs\n'
        'H. Mostrar DNIs\n'
        'I. Frecuencia de elementos\n'
        'J. Exit'
        )
    operacion = input('Que operacion desea ejectutar? ')
    op = operacion.lower()
    match op:
        case 'a':
            conj_1 = int(input('De cual conjunto quiere obtener el conjunto numeros unicos? '))
            unicos = obtener_numeros_unicos(conjuntos[conj_1])
            print(f'El conjunto de digitos unicos del conjunto numero {conj_1} es igual a: {unicos}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'b':
            conj_1 = int(input('Elija el primer conjunto para realizar union, DNI_: '))
            conj_2 = int(input('Elija el segundo conjunto para realizar union, DNI_: '))
            union = obtener_union(conjuntos[conj_1], conjuntos[conj_2])
            print(f'DNI_{conj_1} ∪ DNI_{conj_2} = {union}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'c':
            conj_1 = int(input('Elija el primer conjunto para realizar intersección, DNI_: '))
            conj_2 = int(input('Elija el segundo conjunto para realizar intersección, DNI_: '))
            interseccion = obtener_interseccion(conjuntos[conj_1], conjuntos[conj_2])
            print(f'DNI_{conj_1} ∩ DNI_{conj_2} = {interseccion}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'd':
            conj_1 = int(input('Elija el primer conjunto para realizar la diferencia, DNI_: '))
            conj_2 = int(input('Elija el segundo conjunto para realizar la diferencia, DNI_: '))
            diferencia = obtener_diferencia(conjuntos[conj_1], conjuntos[conj_2])
            print(f'DNI_{conj_1} - DNI_{conj_2} = {diferencia}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'e':
            conj_1 = int(input('Elija el primer conjunto para realizar la diferencia simetrica, DNI_: '))
            conj_2 = int(input('Elija el segundo conjunto para realizar la diferencia simetrica, DNI_: '))
            diferencia_simetrica = obtener_diferencia_simetrica(conjuntos[conj_1], conjuntos[conj_2])
            print(f'DNI_{conj_1} Δ DNI_{conj_2} = {diferencia_simetrica}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'f':
            conj_1 = int(input('De cual conjunto quiere obtener la suma total de sus numeros? '))
            suma = obtener_suma(conjuntos[conj_1])
            print(f'La suma total de los digitos del conjunto numero {conj_1} es igual a: {suma}')
            print('#################################################################')
            continuacion(conjuntos)
        case'g':
            solicitar_dnis()
        case'h':
            mostrar_dnis(conjuntos)
        case'i':
            conj_1 = int(input('De cual conjunto quiere obtener la frecuencia de sus elementos? '))
            dni = conjuntos[conj_1]
            resultado_frecuencia = frecuencia(dni)
            print('#################################################################')
            print(f'Conjunto = {dni}\n')
            for i in range(len(resultado_frecuencia[0])):
                print(f'Numero {resultado_frecuencia[0][i]} => Frecuencia: {resultado_frecuencia[1][i]}')
            print('#################################################################')
            continuacion(conjuntos)
        case'j':
            print('Hasta la vista Baby!')

### FUNCIONES OPERACIONES DE CONJUNTOS ###
def obtener_numeros_unicos(dni):
    numeros_unicos = []
    for num in dni:
        if num not in numeros_unicos:
            numeros_unicos.append(num)
    return numeros_unicos
    
def obtener_union(array_1, array_2):
    numeros_vistos = set() # Conjunto para evitar duplicados
    resultado = []
    for num in array_1:
        if num not in numeros_vistos:
            resultado.append(num)
            numeros_vistos.add(num)
    for num in array_2:
        if num not in numeros_vistos:
            resultado.append(num)
            numeros_vistos.add(num)
    return resultado

def obtener_interseccion(array_1, array_2):
    numeros_vistos = set() # Conjunto para evitar duplicados
    resultado = []
    for num in array_1:
        if num in array_2 and num not in numeros_vistos:
            resultado.append(num)
            numeros_vistos.add(num)  # Se marca como agregado
    return resultado
    
def obtener_diferencia(array_1, array_2):
    numeros_vistos = set() # Conjunto para evitar duplicados
    diferencia = []
    for elemento in array_1:
        if elemento not in array_2 and elemento not in numeros_vistos:
            diferencia.append(elemento)
            numeros_vistos.add(elemento)
    return diferencia
    
def obtener_diferencia_simetrica(array_1, array_2):
    numeros_vistos = set() # Conjunto para evitar duplicados
    diferencia_simetrica = []
    for elemento in array_1:
        if elemento not in array_2 and elemento not in numeros_vistos:
                diferencia_simetrica.append(elemento)
                numeros_vistos.add(elemento)
    for elemento in array_2:
        if elemento not in array_1 and elemento not in numeros_vistos:
                diferencia_simetrica.append(elemento)
                numeros_vistos.add(elemento)
    return diferencia_simetrica
    
def obtener_suma(array_1):
    suma = 0
    for elemento in array_1:
        suma += elemento
    return suma    

def frecuencia(dni):
    unicos = []
    frecuencia = []
    respuesta = []
    for num in dni:
        if num in unicos:
            indice = unicos.index(num)
            frecuencia[indice] += 1
        else:
            unicos.append(num)
            frecuencia.append(1)
    respuesta.append(unicos)
    respuesta.append(frecuencia)
    return respuesta


### INICIO DE SISTEMA ###
letr = input('INICIAR SISTEMA? (Y/N): ')
sistema(letr)