from sys import stdin
import Graficas


def mult(matriz, vector):
    v = [0 for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] += matriz[i][j] * vector[j]
    return v


def matrizProbabilities(slits, targets):
    dim = slits + targets + 1
    matriz = [[0 for j in range(dim)] for i in range(dim)]
    # loop
    for i in range(slits + 1, dim):
        matriz[i][i] = 1

    # slits
    for i in range(1, slits + 1):
        matriz[i][0] = round(1 / slits, 3)

    # targets
    j = 1
    i = slits + 1
    m = targets // 2
    m = m - m // 2
    while i <= len(matriz) - (targets // 2) and j <= slits + 1:
        for k in range(i, i + targets // 2):
            matriz[k][j] = round(1 / (targets // 2), 3)
        i = i + m
        j += 1

    return matriz


def pp(matriz):
    for i in range(len(matriz)):
        print(matriz[i], sep='\n')


def main():
    slits = int(stdin.readline().strip())
    targets = int(stdin.readline().strip())
    matriz_proba = matrizProbabilities(slits, targets)
    pp(matriz_proba)
    state_0 = [1] + [0 for i in range(slits + targets)]
    print(state_0)
    v = mult(matriz_proba,state_0)
    print(v)
    Graficas.graph(v)


main()
