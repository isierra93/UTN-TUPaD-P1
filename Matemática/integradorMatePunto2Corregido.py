from datetime import date

### MENU Y SISTEMA ###
def sistema(ltr):
    op_min = ltr.lower()
    if op_min == 'n':
        print('This is the end my friend :(')
    elif op_min == 'y':
        solicitar_anios()
    else:
        ltr = input('La opcion seleccionada no existe. Por favor ingrese Y o N: ')
        sistema(ltr)

def solicitar_anios():
    conjuntos = []
    n = 3 # Setea cantidad de AÑOS a solicitar
    for i in range(1,n):
        anio_integer = int(input(f'Debe ingresar {n-i} años. Por favor ingrese un año valido sin puntos: '))
        conjuntos.insert(i, anio_integer)
    print('#################################################################')
    print(f'Conjunto AÑOS DE NACIMIENTO = {conjuntos}')
    print('#################################################################')
    elegir_operacion(conjuntos)   

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
        'A. Mostrar Pares e Impares\n'
        'B. Verificar Generacion Z\n'
        'C. Verificar años Bisiestos\n'
        'D. Verificar Edades\n'
        'E. Verificar Producto Cartesiano\n'
        'F. Resetear Años\n'
        'G. Mostrar Años\n'
        'H. Exit'
        )
    operacion = input('Que operacion desea ejectutar? ')
    op = operacion.lower()
    match op:
        case 'a':
            respuesta_pares_impares = mostrar_pares_impares(conjuntos)
            print('#################################################################')
            print(f'Dado el conjunto de años de nacimiento ingresados, podemos determinar\nque el numero de nacimientos en años impares es de {respuesta_pares_impares[1]} y el de pares es de {respuesta_pares_impares[0]}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'b':
            respuesta_generacion = generacion(conjuntos)
            if respuesta_generacion[3] == len(conjuntos):
                print('#################################################################')
                print('Todos los años de nacimiento ingresados son del año 2000 en adelante. El grupo se considera "GENERACION Z"')
                print('#################################################################')
            else:
                print('#################################################################')
                print(f'Los años de nacimiento ingresados son heterogeneos, habiendo {respuesta_generacion[0]} "Baby Boomers", {respuesta_generacion[1]} "Generacion X",\n{respuesta_generacion[2]} "Millenials" & {respuesta_generacion[3]} "Generacion Z"')
                print('#################################################################')
            continuacion(conjuntos)
        case 'c':
            conj_bisiestos = bisiesto(conjuntos)
            if len(conj_bisiestos) == 0:
                print('#################################################################')
                print('No se presentan años BISIESTOS en el conjunto ingresado')
                print('#################################################################')
            else:
                print('#################################################################')
                print(f'Tenemos un año especial!\n{conj_bisiestos}')
                print('#################################################################')
            continuacion(conjuntos)
        case 'd':
            conj_edades = edades(conjuntos)
            print('#################################################################')
            print(f'El conjunto edades segun el conjunto de años recibido es {conj_edades}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'e':
            conj_edades = edades(conjuntos)
            conj_cartesiano = cartesiano(conjuntos)
            print('#################################################################')
            print(f'El resultado de realizar el Producto Cartesiano entre el conjunto EDADES = {conj_edades} y el conjunto AÑOS = {conjuntos} es igual a: {conj_cartesiano}')
            print('#################################################################')
            continuacion(conjuntos)
        case 'f':   
            solicitar_anios()
        case 'g':
            print(f'El conjunto de años ingresado es: {conjuntos}')
            continuacion(conjuntos)
        case 'h':
            print('Hasta la vista Baby!')

### FUNCIONES OPERACIONES DE CONJUNTOS ###
def mostrar_pares_impares(array):
    par = 0
    impar = 0
    respuesta = []
    for num in array:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
    respuesta.append(par)
    respuesta.append(impar)
    return respuesta
    
def generacion(array):
    baby_boomers = 0
    generacion_x = 0
    millenials = 0
    generacion_z = 0
    respuesta = []
    for num in array:
        if num <= 1964:
            baby_boomers += 1
        elif 1964 < num <= 1980:
            generacion_x += 1
        elif 1980 < num <= 1996:
            millenials += 1
        else:
            generacion_z += 1
    respuesta.append(baby_boomers)
    respuesta.append(generacion_x)
    respuesta.append(millenials)
    respuesta.append(generacion_z)
    return respuesta

def bisiesto(array):
    bisiestos = []
    for anio in array:
        if (((anio % 4 == 0 and anio % 100 != 0) or (anio % 100 == 0 and anio % 400 == 0)) and anio not in bisiestos):
            bisiestos.append(anio)
    return bisiestos
        
def edades(array):
    edades = []
    actual = date.today().year
    for anio in array:
        edad = actual - anio
        if edad not in edades:
            edades.append(edad)
    return edades

def cartesiano(array):
    array_de_edades = edades(array)
    res_cart = []
    for i in range(len(array)):
        for j in range(len(array_de_edades)):
            res_cart.append((array[i], array_de_edades[j]))
    return res_cart
        
### INICIO DE SISTEMA ###
letr = input('INICIAR SISTEMA? (Y/N): ')
sistema(letr)