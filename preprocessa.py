import numpy as np

def remove_variavel(matriz):
    col = matriz.shape[1]
    for i in range(col):
        if len(np.where(matriz[:,i]==1)[0]) == 1:
            new_matriz = np.delete(matriz,i,1)
        else:
            new_matriz = matriz
    print(new_matriz)