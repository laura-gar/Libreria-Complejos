import numpy as np
import matplotlib.pyplot as plt
import math
from ComplexLib import*

def graph(v):
    N = len(v)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.5  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, v, width)

    plt.ylabel('Percentages')
    plt.title('Probabilities for a state vector')
    plt.xticks(ind)
    plt.yticks(np.arange(0, 1.1, 0.1))

    plt.show()


def sumaComplejos(a, b):
    c = a[0] + b[0]
    d = a[1] + b[1]
    return (round(c,3), round(d,3))


def productoComplejos(a, b):
    c = a[0] * b[0] - a[1] * b[1]
    d = a[0] * b[1] + a[1] * b[0]
    return (c, d)


def action(matriz, vector):
    v = [(0, 0) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] = sumaComplejos(v[i], productoComplejos(matriz[i][j], vector[j]))
    return v

def cuadrados(a):
    return a[0]**2 + a[1]**2

def values(n):
    t = [(0, 0) for i in range(4)]
    k = 0
    while k <= n:
        for i in range(2):
            for j in range(2):
                val = (round((-1) ** (i + 1) * (math.sqrt(n) / n), 3), round((-1) ** (j + i) * (math.sqrt(n) / n), 3))
                t[0 + k] = val
                k += 1
    return t


def matrizProbabilitiesC(slits, targets):
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

def verify(matriz):
    v = [0 for i in range(len(matriz[0]))]
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[0])):
            suma = suma + cuadrados(matriz[j][i])
        v [i] = suma
    return v

def pp(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def prob(lista):
    for i in range(len(lista)):
        lista[i] = cuadrados(lista[i])

    return lista

def expQuantic(slits, targets, clicks):
    matriz = matrizProbabilitiesC(slits,targets)
    print('Matriz de Probabilididades')
    pp(matriz)
    state = [(1,0)] + [(0,0) for i in range(len(matriz)-1)]
    for i in range(clicks):
        state = action(matriz, state)
    print('Final state')
    print(state)
    graph(prob(state))




def main():
    print(expQuantic(2,5,2))


main()