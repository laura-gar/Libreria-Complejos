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
