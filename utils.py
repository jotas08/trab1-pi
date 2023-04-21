import numpy as np
from preprocessa import  remove_variavel

def ler_instancia(file):
    instancia = np.loadtxt(file, dtype = str)
    instancia = np.array([list(map(int,row))for row in instancia])
    return instancia



if __name__ == '__main__':
    matriz = ler_instancia('entrada.txt')
    print(matriz)
    remove_variavel(matriz)


