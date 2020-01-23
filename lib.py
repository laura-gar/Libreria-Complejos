##LIBRERIA COMPLEJOS
##Laura Garcia
##CNYT

from sys import stdin
import math

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

def multiplicacion(a,b):
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
        ang = (math.atan(a[1]/a[0])+(math.pi))
    else:
        ang = math.atan(a[1]/a[0])
    ang = ang * 180/math.pi
    return ang

def cartToPol(a):
    '''Función que encuentra las coordenadas polares de un número complejo
       (tupla de float) -> (tupla de float)'''
    p = modulo(a)
    ang = returnPhase(a)
    return (p,ang)

def sumaVectorial(v1,v2):
    vector = []
    for i in range(len(v1)):
        vector += [suma(v1[i],v2[i])]
    return vector
    
def inverso(v1):
    for i in range(len(v1)):
        a1 = v1[i][0]*-1
        b1 = v1[i][1]*-1
        v1[i] = (a1,b1)
    return v1

def productoEscalar(c,v1):
    vector = []
    for i in range(len(v1)):
        vector += [multiplicacion(c,v1[i])]
    return vector

def sumaMatrices(m1,m2):
    matriz = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila += [suma(m1[i][j],m2[i][j])]
        matriz += [fila]
    return matriz

def inversoMatrices(m1):
    matriz = []
    for i in range(len(m1)):
        matriz += [inverso(m1[i])]
    return matriz

def multEscalarMatriz(c, m1):
    matriz = []
    for i in range(len(m1)):
        matriz += [productoEscalar(c,m1[i])]
    return matriz

def transpuesta(m1):
    matriz = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            matriz += [m1[j][i]]
    return matriz

def matrizConjugada(m1):
    matriz = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            matriz += conjugado(m1[i][j])
    return matriz

def matrizAdjunta(m1):
    m = matrizConjugada(transpuesta(m1))
    return m 
    
                   
