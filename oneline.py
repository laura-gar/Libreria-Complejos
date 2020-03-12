from sys import stdin
import math
from ComplexLib import*
def modsquare(a):
    return a[0]**2 + a[1]**2

def magVector(v1):
    suma = 0
    for i in range(len(v1)):
        suma += modsquare(v1[i])
    return math.sqrt(suma)

def innerP(v1, v2):
    suma = (0,0)
    for i in range(len(v2)):
        v2[i] = conjugado(v2[i])
    for i in range(len(v1)):
        suma = sumaComplejos(suma, productoComplejos(v2[i], v1[i]))

    return suma

def probability(vector, position):
    a = modsquare(vector[position])
    print((a/magVector(vector))*100)

def normalized(v1):
    a = magVector(v1)
    for i in range(len(v1)):
        v1[i] = divisionComplejos(v1[i],(a,0))
    return v1

def action(matriz, vector):
    v = [(0, 0) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] = sumaComplejos(v[i], productoComplejos(matriz[i][j], vector[j]))
    return v
def escalarmatriz(c, m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = productoComplejos(c, m[i][j])
    return m

def identidad(n):
    matriz = [[(0,0) for i in range(n)] for j in range(n)]
    for i in range(n):
        matriz[i][i] = (1,0)
    return matriz
        
def expectedValue(obs, state):
    return innerP(action(obs, state),state)

def varianza(omega, vector):
    ide = identidad(len(vector))
    e = expectedValue(omega, vector)
    delta = escalarmatriz(e, ide)
    print(delta)
    delta = restaMatrices(omega, delta)
    pro = productoMatrices(delta, delta)
    print(pro)
    var = expectedValue(productoMatrices(delta, delta), vector)
    return var

def main():
    #matriz = [[(2,0),(1,1)],[(1,-1),(3,0)]]
    #vector = [(1/math.sqrt(2),0),(0,1/math.sqrt(2))]
    matriz = [[(1,0),(0,-1)],[(0,1),(2,0)]]
    vector = [(math.sqrt(2)/2,0),(0,math.sqrt(2)/2)]
    a = action(matriz, vector)
    #print(round(innerP(a,vector)[0], 2))
    print(varianza(matriz, vector))

main()
