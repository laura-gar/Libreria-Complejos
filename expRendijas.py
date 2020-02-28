from sys import stdin
def matrizProbabilidades(slits,targets):
    dim = slits + targets + 1
    matriz =[[0 for j in range(dim)] for i in range(dim)]
    #loop
    for i in range(slits + 1,dim):
        matriz[i][i] = 1

    #slits
    for i in range(1,slits + 1):
        matriz[i][0] = round(1 / slits,3)

    #targets
    j = 1
    i = slits+ 1
    m = targets//2
    m = m - m//2
    while i <= len(matriz)-(targets//2) and j <= slits + 1:
        for k in range(i,i+targets//2):
            matriz[k][j] = round(1/(targets//2),3)
        #pp(matriz)
        i = i + m
        j += 1

    pp(matriz)


    #PrettyPrint
    # for i in range(len(matriz)):
    #     print(matriz[i],sep= ' ')

def pp(matriz):
    for i in range(len(matriz)):
        print(matriz[i], sep='\n')

def main():
    slits = int(stdin.readline().strip())
    targets = int(stdin.readline().strip())
    matrizProbabilidades(slits,targets)
main()