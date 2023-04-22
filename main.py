"""Equipe 
Thais Majory - 473177
João Paulo - [bota tua matricula aqui jotinha]"""

#from guloso import greedy_algorithm
from preprocessa import *
from utils import ler_instancia

if __name__ == '__main__':
    print('Loading...')
    matriz = ler_instancia('entrada.txt')
    # preprocessamento
    print(matriz,'\n',matriz.shape)
    matriz,sol = etapa1(matriz)
    print(matriz,'\n',matriz.shape)
    matriz = etapa2(matriz)
    print(matriz,'\n',matriz.shape)

    # algoritmo guloso

    # greedy_algorithm()



