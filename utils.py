import numpy as np


def ler_instancia(file):
    instancia = np.loadtxt(file, dtype = str)
    instancia = np.array([list(map(int,row))for row in instancia])
    return instancia

"""Método que busca, remove e retorna a restricão das variáveis que podem ser removidas na primeira etapa do preprocessamento"""
def remove_variavel(matriz): 
    lista_restricoes = []
    variaveis_sol=[]
    row = matriz.shape[0]
    for i in range(row):
        if len(np.where(matriz[:,i] == 1 )[0]) == 1 :
            lista_restricoes.append(np.where(matriz[:,i] == 1 )[0][0])
            matriz = np.delete(matriz,i,1)
            variaveis_sol.append(i+1)
        return matriz,lista_restricoes, variaveis_sol

"""Método de remoção das restrições atreladas as variáveis"""
def remove_restricao(matriz,lista):
    if lista != None:
        for i in lista:
            matriz = np.delete(matriz, i , 0)
    return matriz


def acha_subconj(row1,row2):
    return  all(x ==  0 or  y ==1 for x,y in  zip(row1,row2))


def remove_redundante(matriz):
    row = matriz.shape[0]
    for i in range(row):
        if i+1 < matriz.shape[0]:
            if acha_subconj(matriz[i],matriz[i+1]):
                matriz = remove_restricao(matriz, [i])
                row -= 1
            elif acha_subconj(matriz[i+1],matriz[i]):
                matriz = remove_restricao(matriz,[i+1])
                row -= 1
    return matriz