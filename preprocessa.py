import numpy as np

"""Método que busca, remove e retorna a restricão das variáveis que podem ser removidas na primeira etapa do preprocessamento"""
def remove_variavel(matriz): 
    lista_restricoes = []
    col = matriz.shape[1]
    for i in range(col):
        if len(np.where(matriz[:,i] == 1 )[0]) == 1 :
            lista_restricoes.append(np.where(matriz[:,i] == 1 )[0][0])
            matriz = np.delete(matriz,i,1)
        return matriz,lista_restricoes

"""Método de remoção das restrições atreladas as variáveis"""
def remove_restricao(matriz,lista):
    print(lista)
    if lista != None:
        for i in lista:
            print(i)
            matriz = np.delete(matriz, i , 0)
    return matriz