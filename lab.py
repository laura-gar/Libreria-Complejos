import math
def prodTensorMatrices(m1,m2):
    m, mp, n, np = len(m1),len(m1[0]),len(m2), len(m2[0])
    matriz = [[0 for j in range(mp*np)] for i in range(m*n)]
    for j in range(m*n):
        for k in range(mp*np):
            matriz[j][k] = m1[j//n][k//m] * m2[j%n][k%n]
    return matriz

def multMatRea(m1, m2):
    matriz = [[0 for j in range(len(m2[0]))]for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                matriz[i][j] += m1[i][k]*m2[k][j]
    return matriz

def simulacion():
    v1 = [[1],[0],[0],[0]]
    x = [[0,1],[1,0]]
    h = [[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]]
    '''Se realiza el producto tensor entre X y H'''
    m1 = prodTensorMatrices(x,h)

    '''Se realiza el rpoducto tensor entre H y H '''
    m2 = prodTensorMatrices(h,h)

    '''Se realiza la multiplicaion entre m1 y m2'''
    q = multMatRea(m2,m1)

    '''Se multiplica el vector del qbit por la matriz resultante'''

    q1 = multMatRea(q,v1)
    print(q1)

    

def main():
    v1 = [[1],[0],[0],[0]]
    x = [[0,1],[1,0]]
    h = [[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]]
    exp(h,x,v1)
main()
