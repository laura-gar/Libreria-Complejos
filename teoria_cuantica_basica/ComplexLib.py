# LIBRERIA COMPLEJOS
# Laura Garcia
# CNYT

import math
import numpy as np
import matplotlib.pyplot as plt


def sumaComplejos(a, b):
    '''Función que suma dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = a[0] + b[0]
    d = a[1] + b[1]
    return (round(c,3), round(d,3))


def restaComplejos(a, b):
    '''Función que resta dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = a[0] - b[0]
    d = a[1] - b[1]
    return (c, d)


def productoComplejos(a, b):
    '''Función que multiplica dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = a[0] * b[0] - a[1] * b[1]
    d = a[0] * b[1] + a[1] * b[0]
    return (c, d)


def divisionComplejos(a, b):
    '''Función que divide dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = (a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2)
    d = (a[1] * b[0] - a[0] * b[1]) / (b[0] ** 2 + b[1] ** 2)
    return (c, d)


def modulo(a):
    '''Función que encuentra el modulo de un número complejo
       (tupla de float) -> (float)'''
    mod = round(math.sqrt(a[0] ** 2 + a[1] ** 2), 2)
    return mod


def conjugado(a):
    '''Función que encuentra el conjugado de un número complejo
       (tupla de float) -> (tupla de float)'''
    conj = (a[0], -a[1])
    return conj


def returnPhase(a):
    '''Función que encuentra el angulo de un número complejo
       (tupla de float) -> (float)'''
    ang = None
    if (a[0] < 0 and a[1] > 0) or (a[0] < 0 and a[1] < 0):
        ang = round((math.atan(a[1] / a[0]) + (math.pi)), 2)
    elif a[0] > 0 and a[1] < 0:
        ang = round((math.atan(a[1] / a[0]) + 2 * math.pi), 2)
    else:
        ang = round(math.atan(a[1] / a[0]), 2)
    return ang


def cartToPol(a):
    '''Función que encuentra las coordenadas polares de un número complejo
       (tupla de float) -> (tupla de float)'''
    p = modulo(a)
    ang = returnPhase(a)
    return (p, ang)


def inverso(a):
    a1 = a[0] * -1
    b1 = a[1] * -1
    return (a1, b1)


def sumaVectores(v1, v2):
    '''Función que realiza la suma de dos vectores con números complejos
       (lista,lista)->(lista)'''
    vector = []
    for i in range(len(v1)):
        vector += [sumaComplejos(v1[i], v2[i])]
    return vector


def restaVectores(v1, v2):
    '''Función que realiza la suma de dos vectores con números complejos
       (lista,lista)->(lista)'''
    vector = []
    for i in range(len(v1)):
        vector += [restaComplejos(v1[i], v2[i])]
    return vector


def inversoVectores(v1):
    '''Función que convierte un vector en su inverso
       (lista)->(lista)'''
    for i in range(len(v1)):
        v1[i] = inverso(v1[i])
    return v1


def escalarPorVector(c, v1):
    '''Función que multiplica un número complejo por un
       vector de números complejos
       (tupla de float, lista)->(lista)'''
    vector = []
    for i in range(len(v1)):
        vector += [productoComplejos(c, v1[i])]
    return vector


def sumaMatrices(m1, m2):
    '''Función que realiza la suma de dos matrices de números complejos
       (matriz,matriz)->(matriz)'''
    if len(m1) == len(m2) and len(m1[0]) == len(m2[1]):
        matriz = [[0 for j in range(len(m1[0]))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                matriz[i][j] = sumaComplejos(m1[i][j], m2[i][j])
        return matriz
    else:
        print('Error')


def restaMatrices(m1, m2):
    '''Función que realiza la suma de dos matrices de números complejos
       (matriz,matriz)->(matriz)'''
    if len(m1) == len(m2) and len(m1[0]) == len(m2[1]):
        matriz = [[0 for j in range(len(m1[0]))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                matriz[i][j] = restaComplejos(m1[i][j], m2[i][j])
        return matriz
    else:
        print('Error')


def inversoMatrices(m1):
    '''Función que convierte una matriz en su inverso
       (matriz)->(matriz)'''
    matriz = [[0 for j in range(len(m1[0]))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz[i][j] = inverso(m1[i][j])
    return matriz


def escalarPorMatriz(c, m1):
    '''Función que multiplica un número complejo por una
       matriz de números complejos
       (tupla de float, matriz)->(matriz)'''
    matriz = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz += [productoComplejos(c, m1[i][j])]
    return matriz


def transpuesta(m1):
    '''Función que cambia filas por columnas y hace la matriz transpuesta
       (matriz)->(matriz)'''
    matriz = []
    for i in range(len(m1[0])):
        fila = []
        for j in range(len(m1)):
            fila += [m1[j][i]]
        matriz += [fila]
    return matriz


def matrizConjugada(m1):
    '''Función que convierte cada elemento de la matriz en su conjugado
       (matriz)->(matriz)'''
    matriz = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila += [conjugado(m1[i][j])]
        matriz += [fila]
    return matriz


def matrizAdjunta(m1):
    '''Función que hace la matriz adjunta
       (matriz)->(matriz)'''
    m = matrizConjugada(transpuesta(m1))
    return m


def productoMatrices(m1, m2):
    '''Función que realiza el producto de dos matrices complejas de tamaños compatibles
       (matriz,matriz)->(matriz)'''
    matriz = [[(0, 0) for j in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                matriz[i][j] = sumaComplejos(matriz[i][j], productoComplejos(m1[i][k], m2[k][j]))
    return matriz


def action(m1, v1):
    '''Función que encuentra la acción que realiza una matriz sobre un vector
       (matriz,matriz)->(matriz)'''
    v = productoMatrices(m1, v1)
    return v


def innerProduct(v1, v2):
    '''Función que realiza el producto interno de dos vectores
       (lista,lista)->(float)'''
    res = productoMatrices(matrizAdjunta(v1), v2)
    return res[0][0][0]


def norma(v1):
    '''Función que calcula la norma de un vector
       (matriz)->(float)'''
    norm = math.sqrt(innerProduct(v1, v1))
    return round(norm, 2)


def distanciaVectores(v1, v2):
    '''Función que calcula la distancia entre dos vectores
       (matriz,matriz)->(float)'''
    res = math.sqrt(innerProduct(restaMatrices(v1, v2), restaMatrices(v1, v2)))
    return round(res, 2)


def matrizUnitary(m1):
    '''Función que muestra si la matriz es unitaria
       (matriz)->(bool)'''
    matId = [[(0, 0) for j in range(len(m1))] for i in range(len(m1))]
    for i in range(len(m1)):
        matId[i][i] = (1, 0)
    a, b, c = productoMatrices(m1, matrizAdjunta(m1)), productoMatrices(matrizAdjunta(m1), m1), matId
    if a == b == c:
        return True
    else:
        return False


def matrizHermitiana(m1):
    '''Función que muestra si la matriz es Hermitiana
       (matriz)->(bool)'''
    return (m1 == matrizAdjunta(m1))


def productoTensor(m1, m2):
    '''Función que calcula el producto tensor de dos matrices o vectores complejos
       (matriz,matriz)->(matriz)'''
    filas, columnas = len(m1), len(m1[0])
    filas1, columnas1 = len(m2), len(m2[0])
    matriz = [[(0,0) for j in range(columnas*columnas1)] for i in range(filas*filas1)]
    for i in range(filas):
        for j in range(columnas):
             for k in range(filas1):
                  for l in range(columnas1):
                       matriz[len(m2)*i+k][len(m2)*j+l] = productoComplejos(m1[i][j],m2[k][l])
    return matriz 

## Version 3

def graph(v):
    '''Función que gráfica las probabilidades de los estados'''
    N = len(v)

    ind = np.arange(N)
    width = 0.8
    p1 = plt.bar(ind, v, width)
    plt.ylabel('Percentages')
    plt.title('Probabilities for a state vector')
    plt.xticks(ind)
    plt.yticks(np.arange(0, 1.1, 0.1))

    plt.show()


def mult(matriz, vector):
    v = [0 for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] += round(matriz[i][j] * vector[j],2)
    return v


def matrizProbabilities(slits, targets):
    '''Función que genera una matriz de probabilidades'''
    dim = slits + targets + 1
    matriz = [[0.0 for j in range(dim)] for i in range(dim)]
    # loop
    for i in range(slits + 1, dim):
        matriz[i][i] = 1.0

    # slits
    for i in range(1, slits + 1):
        matriz[i][0] = round(1 / slits, 3)

    # targets
    j = 1
    i = slits + 1
    if slits%2 == 0:
        m1 = (targets + 1) //2
        m2 = m1 - m1 //2
    else:
        m1 = targets  // 2
        m2 = m1 - m1 // 2

    while i <= len(matriz) - m1 and j < slits + 1:
        for k in range(i,  i + m1):
            matriz[k][j] = round(1 / (m1), 2)
        i = i + m2
        j += 1

    return matriz


def action2(matriz, vector):
    '''Función que calcula la acción de una matriz sobre un vector'''
    v = [(0, 0) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] = sumaComplejos(v[i], productoComplejos(matriz[i][j], vector[j]))
    return v


def cuadrados(a):
    '''Funcion que retorna el cuadrado de los componentes de un número complejo'''
    return a[0]**2 + a[1]**2


def values(n):
    '''Función que calcula los valores que son necesrios para la matriz de probabilidades compleja'''
    t = [(0, 0) for i in range(4)]
    k = 0
    while k <= n:
        for i in range(2):
            for j in range(2):
                val = (round((-1) ** (i + 1) * (1/math.sqrt(2*n)), 3), round((-1) ** (j + i) * (1/math.sqrt(2*n)), 3))
                t[0 + k] = val
                k += 1
    return t


def matrizProbabilitiesC(slits, targets):
    '''Función que genera la matriz de probabilidades complejas'''
    dim = slits + targets + 1
    matriz = [[(0, 0) for j in range(dim)] for i in range(dim)]
    # loop
    for i in range(slits + 1, dim):
        matriz[i][i] = (1,0)

    # slits
    for i in range(1, slits + 1):
        val = round(1 / math.sqrt(slits), 3)
        matriz[i][0] = (val,0)

    # targets
    j = 1
    i = slits + 1
    if slits % 2 == 0:
        m1 = (targets + 1) // 2
        m2 = m1 - m1 // 2
    else:
        m1 = targets // 2
        m2 = m1 - m1 // 2
    t = values(m1)
    while i <= len(matriz) - m1 and j < slits + 1:
        y = 0
        for k in range(i, i + m1):
            matriz[k][j] = sumaComplejos(matriz[k][j],t[y])
            y += 1
        i = i + m2
        j += 1

    return matriz


def pp(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def prob(lista):
    for i in range(len(lista)):
        lista[i] = cuadrados(lista[i])
    return lista


def clasToQuan(matriz, vector, clicks):
    '''Función que calcula el estado final de un vector luego de cierto número de clicks con coeficientes booleanos'''
    for i in range(clicks):
        vector = mult(matriz, vector)
    graph(vector)
    return vector


def expRendijas(slits, targets, clicks):
    '''Función que calcula el vector final luego de cierta cantidad de clicks de manera probabílistica'''
    matriz = matrizProbabilities(slits, targets)
    v = [1] + [0 for i in range(len(matriz) - 1)]
    for i in range(clicks):
        v = mult(matriz, v)
    graph(v)
    return v


def expQuantic(slits, targets, clicks):
    '''Función que calcula el vector final luego de cierta cantidad de clicks de manera probabílistica compleja'''

    matriz = matrizProbabilitiesC(slits,targets)
    state = [(1,0)] + [(0,0) for i in range(len(matriz)-1)]
    for i in range(clicks):
        state = action2(matriz, state)
    return state
    graph(prob(state))

