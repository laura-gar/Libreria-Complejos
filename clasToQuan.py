from sys import stdin
import Graficas
def mult (matriz, vector):
    v = [0 for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v [i] += matriz[i][j] * vector[j]
    return v

def endstate(matriz, vector, clicks):
    for i in range(clicks):
        vector = mult(matriz,vector)
    return vector

def main():
    dim = int(stdin.readline().strip())
    matrizState = [[]for i in range(dim)]
    for i in range(dim):
        matrizState[i] = [int(x) for x in stdin.readline().strip().split(' ')]
    state_0 = [int(x) for x in stdin.readline().strip().split(' ')]
    clicks = int(stdin.readline().strip())
    final = endstate(matrizState,state_0,clicks)
    Graficas.graph(final)

main()
