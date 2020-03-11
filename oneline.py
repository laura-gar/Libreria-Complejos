from ComplexLib import*
def modsquare(a):
    return a[0]**2 + a[1]**2

def innerP(v1, v2):
    suma = (0,0)
    for i in range(len(v2)):
        v2[i] = conjugado(v2[i])
    print(v2)
    for i in range(len(v1)):
        suma = sumaComplejos(suma, productoComplejos(v2[i], v1[i]))

    return suma

def probability(vector, position):
    suma = 0
    for i in range(len(vector)):
        suma += modsquare(vector[i])
    a = modsquare(vector[position])
    print(a, suma)
    print(a/suma)

def main():
    v1 = [(1,1), (3,2)]
    v2 = [(2, -5), (5, 2)]
    print(innerP(v1, v2))
main()