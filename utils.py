import numpy as np

def ler_instancia(file):
    instancia = np.loadtxt(file, dtype = str)
    instancia = np.array([list(map(int,row))for row in instancia])
    return instancia


def pertence(matriz,i):
    return np.where(matriz[:,i]==1)[0]  


if __name__ == '__main__':
    matriz = ler_instancia('entrada.txt')
    if len(pertence(matriz,1)) == 1:
        print('está contido em apenas 1 subconjunto')



