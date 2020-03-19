from ComplexLib import *

def act(matriz, vector):
    '''Función que calcula la acción de una matriz sobre un vector'''
    v = [(0, 0) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] = sumaComplejos(v[i], productoComplejos(matriz[i][j], vector[j]))
    return v

def modsquare(a):
    '''Función que eleva al cuadrado las componentes de el número complejo'''
    return a[0] ** 2 + a[1] ** 2


def magVector(v1):
    '''Función que encuentra el la magnitud del vector'''
    suma = 0
    for i in range(len(v1)):
        suma += modsquare(v1[i])
    return math.sqrt(suma)


def innerP(v1, v2):
    '''Función que realiza el producto interno entre dos vectores'''
    suma = (0, 0)
    for i in range(len(v2)):
        v2[i] = conjugado(v2[i])
    for i in range(len(v1)):
        suma = sumaComplejos(suma, productoComplejos(v2[i], v1[i]))

    return suma


def probability(vector, position):
    '''Función que encuentra la probabilidad de observar una particula en una posicion luego de observarlo'''
    suma = 0
    for i in range(len(vector)):
        suma += modsquare(vector[i])
    a = modsquare(vector[position])
    return round((a / suma) * 100, 2)


def normalized(v1):
    '''Función que convierte los vectores en vectores unitarios'''
    a = magVector(v1)
    for i in range(len(v1)):
        v1[i] = divisionComplejos(v1[i], (a, 0))
    return v1


def amplitudTransicion(v1, v2):
    '''Encuentra la probabilidad de pasar de un estado a otro luego de ser observado'''
    return innerP(normalized(v1), normalized(v2))


