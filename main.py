"""Equipe 
Thais Majory - 473177
João Paulo - 427451"""
from guloso import minimum_set_cover
from preprocessa import *
from utils import ler_instancia

if __name__ == '__main__':
    matriz = ler_instancia('entrada.txt')
    matriz,sol = etapa1(matriz)
    matriz = etapa2(matriz)
    matriz = etapa3(matriz)
    solu = minimum_set_cover(matriz, len(matriz))
    print(solu)