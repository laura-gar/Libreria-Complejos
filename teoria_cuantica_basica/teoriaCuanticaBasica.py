from ComplexLib import *
import sympy
import numpy
import math
import cmath
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


def expectedValue(obs, state):
    '''Función que encuentra el valor esperado entre un observador y un estado inicial'''
    m1 = action2(obs, state)
    return (innerP(m1, state))[0]


def identity(n, val):
    '''Función que crea la matriz identidad y tiene como parametro el valor esperado'''
    matriz = [[(0,0) for j in range(n)] for i in range(n)]
    for i in range(n):
        matriz[i][i] = (val,0)
    return matriz

def varianza(obs, state):
    '''Función que encuentra la varianza entre un observador y un estado inicial'''
    s1 = list(state)
    m1 = restaMatrices(obs, identity(len(state), expectedValue(obs, state)))
    m2 = productoMatrices(m1,m1)
    m3 = innerP(action2(m2, s1), s1)
    return m3[0]


def med_var(observator, state):
    '''Función que encuentra la varianza y la media'''
    if matrizHermitiana(observator):
        print('MEDIA', expectedValue(observator, state))
        print('VARIANZA', varianza(observator, state))
    else:
        print('El observador no es una una matriz hermitiana')


def eigenValues(eValues):
    '''Función que encuentra los valores propios de una matriz'''
    lst = []
    min, max = -100, 100
    for i in range(min, max):
        if eValues.get(i) is not None:
            lst += [i]
    return lst


def eigenVectors(eVector):
    '''Función que halla los vectores propios de una matriz'''
    lst = []
    for i in range(len(eVector)):
        n = complex(eVector[i])
        x, y = int(n.real), int(n.imag)
        lst += [(x, y)]
    return lst


def convMatriz(m):
    '''Función que convierte una matriz de tuplas en una matriz de números complejos'''
    m1 = [[0 for j in range(len(m[0]))] for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m1[i][j] = complex(m[i][j][0], m[i][j][1])
    return m1


def prob(matriz, state,):
    '''Función que halla la probabilidad de que un estado llegue a un vector propio'''
    eValues, eVector = reviewObs(matriz, state)
    if expectedValue(matriz, state) in eValues:
        print('Probabilidad de llegar a un vector propio 100%')
    else:
        if type(eVector[0]) == list:
            for i in range(len(eVector)):
                return amplitudTransicion(state, eVector[i])
        else:
            return amplitudTransicion(state, eVector)


def reviewObs(m1, state):
    '''Función que revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.'''
    a = convMatriz(m1)
    a = sympy.Matrix(a)
    eValues = a.eigenvals()
    eValues = eigenValues(eValues)
    x, v = a.eigenvects()[0][2][0], a.eigenvects()[0][0]
    eVectors = x*v
    eVector = eigenVectors(eVectors)
    return eValues, eVector

def dynamic(n, matriz, state):
    '''Función quhe calcula la posicion de una particula luego de que recorra una serie de matrices unitarias'''
    for i in range(n):
        state = act(matriz, state)
    return state
