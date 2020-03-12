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

def amplitudTransicion(v1, v2):
    return innerP(normalized(v1), normalized(v2))

def main():
    v1 = [(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
    v2 = [(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]
    print(amplitudTransicion(v1,v2))

main()
