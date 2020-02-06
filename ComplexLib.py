##LIBRERIA COMPLEJOS
##Laura Garcia
##CNYT

from sys import stdin
import math
math.tan

def suma(a,b):
    '''Función que suma dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = a[0] + b[0]
    d = a[1] + b[1]
    return(c,d)

def resta(a,b):
    '''Función que resta dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = a[0] - b[0]
    d = a[1] - b[1]
    return (c,d)

def multCom(a,b):
    '''Función que multiplica dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = a[0]*b[0] - a[1]*b[1]
    d = a[0]*b[1] + a[1]*b[0]
    return (c,d)

def division(a,b):
    '''Función que divide dos números complejos
       (tupla de float,tupla de float) -> (tupla de float)'''
    c = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
    d = (a[1]*b[0] - a[0]*b[1]) / (b[0]**2 + b[1]**2)
    return (c,d)

def modulo(a):
    '''Función que encuentra el modulo de un número complejo
       (tupla de float) -> (float)'''
    mod = round(math.sqrt(a[0]**2 + a[1]**2),2)
    return mod

def conjugado(a):
    '''Función que encuentra el conjugado de un número complejo
       (tupla de float) -> (tupla de float)'''
    conjA = (a[0],-a[1])
    return conjA

def returnPhase(a):
    '''Función que encuentra el angulo de un número complejo
       (tupla de float) -> (float)'''
    ang = None
    if (a[0]<0 and a[1]>0) or (a[0]<0 and a[1]<0):
        ang = round((math.atan(a[1]/a[0])+(math.pi)),2)
    elif a[0]>0 and a[1]<0:
        ang = round((math.atan(a[1]/a[0])+2*(math.pi)),2)
    else:
        ang = round(math.atan(a[1]/a[0]),2)
    return ang

def cartToPol(a):
    '''Función que encuentra las coordenadas polares de un número complejo
       (tupla de float) -> (tupla de float)'''
    p = modulo(a)
    ang = returnPhase(a)
    return (p,ang)

def sumaVectorial(v1,v2):
    '''Función que realiza la suma de dos vectores con números complejos
       (lista,lista)->(lista)'''
    vector = []
    for i in range(len(v1)):
        vector += [suma(v1[i],v2[i])]
    return vector

def inverso(v1):
    '''Función que convierte un vector en su inverso
       (lista)->(lista)'''
    for i in range(len(v1)):
        a1 = v1[i][0]*-1
        b1 = v1[i][1]*-1
        v1[i] = (a1,b1)
    return v1

def productoEscalar(c,v1):
    '''Función que multiplica un número complejo por un
       vector de números complejos
       (tupla de float, lista)->(lista)'''
    vector = []
    for i in range(len(v1)):
        vector += [multCom(c,v1[i])]
    return vector

def sumaMatrices(m1,m2):
    '''Función que realiza la suma de dos matrices de números complejos
       (matriz,matriz)->(matriz)'''
    if len(m1)==len(m2) and len(m1[0])==len(m2[1]):
        matriz = [[0 for j in range(len(m1[0]))]for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                matriz[i][j]= suma(m1[i][j],m2[i][j])
            
        return matriz
    else:
        print('Error')

def inversoMatrices(m1):
    '''Función que convierte una matriz en su inverso
       (matriz)->(matriz)'''
    matriz = []
    for i in range(len(m1)):
        matriz += [inverso(m1[i])]
    return matriz

def multEscalarMatriz(c, m1):
    '''Función que multiplica un número complejo por una
       matriz de números complejos
       (tupla de float, matriz)->(matriz)'''
    matriz = []
    for i in range(len(m1)):
        matriz += [productoEscalar(c,m1[i])]
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

def multMatCom(m1, m2):
    matriz = [[(0,0) for j in range(len(m2[0]))]for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                matriz[i][j] = suma(matriz[i][j],multCom(m1[i][k],m2[k][j]))
    return matriz

def multMatRea(m1, m2):
    matriz = [[0 for j in range(len(m2[0]))]for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                matriz[i][j] += m1[i][k]*m2[k][j]
    return matriz

def innerInt(v1,v2):
    res = multMatRea(transpuesta(v1),v2)
    return res[0][0]

def innerProduct(v1,v2):
    print(matrizAdjunta(v1))
    res = multMatCom(matrizAdjunta(v1),v2)
    return res[0][0]

def normaVector(v1):
    norma = math.sqrt(innerProduct(v1,v1))
    return norma

def matrizHermitain(m1):
    return (m1 == matrizAdjunta(m1))

def matrizUnitary(m1):
    matId = [[(0,0) for j in range(len(m1))]for i in range(len(m1))]
    for i in range(len(m1)):
        matId[i][i] = (1,0)
    print(matId)
    a, b, c = multMatCom(m1,matrizAdjunta(m1)),multMatCom(matrizAdjunta(m1),m1), matId
    print(a)
    if a == b == c:
        return True
    else:
        return False

def prodTensor(v1,v2):
    tensor = [(0,0) for i in range(len(v1)*len(v2))]
    pos = 0
    for i in range(len(v1)):
        for j in range(len(v2)):
            tensor[pos] = v1[i]*v2[j]
            pos += 1
    return tensor

def prodTensorMatrices(m1,m2):
    m, mp, n, np = len(m1),len(m1[0]),len(m2), len(m2[0])
    matriz = [[0 for j in range(mp*np)] for i in range(m*n)]
    for j in range(m*n):
        for k in range(mp*np):
            matriz[j][k] = m1[j//n][k//m] * m2[j%n][k%n]
    return matriz
