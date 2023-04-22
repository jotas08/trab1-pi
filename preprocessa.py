from utils import *

def etapa1(matriz):
    matriz,var,sol = remove_variavel(matriz)
    matriz = remove_restricao(matriz,var)
    return matriz,sol

def etapa2(matriz):
    return remove_redundante(matriz)