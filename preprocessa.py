from utils import *

#Objeto pertence a apenas um dos subconjuntos Sj.
#Variável x_j é removida, como também 
#a restrição que a envolva
def etapa1(matriz):
    matriz,var,sol = remove_variavel(matriz)
    matriz = remove_restricao(matriz,var)
    return matriz,sol

#Restrição implica numa outra.
#Quando objetos e_i são cobertos pelo subconjunto e_j,
#nesse caso removemos a restrição que contém e_i
def etapa2(matriz):
    return remove_redundante(matriz)

def etapa3(matriz):
    matriz_b,sol = etapa1(matriz)
    etapa2(matriz_b)
    return rm_redundant_subconj(matriz_b)