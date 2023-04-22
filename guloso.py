def minimum_set_cover(S, F):
    C = set()
    U = set(S)

    while U:
        # Encontrar o subconjunto Sj em F com a maior quantidade de elementos não cobertos em U
        best_subset = max(F, key=lambda Sj: len(U & Sj))
        C.add(best_subset)
        
        U -= best_subset

        # Remover o subconjunto selecionado da lista de subconjuntos F
        F.remove(best_subset)

        # Atualizar os subconjuntos restantes em F removendo os elementos cobertos por C
        F = [Sj - best_subset for Sj in F if len(Sj - best_subset) > 0]

    return C

# def greedy_algorithm(conj_s, f):
#     c = []
#     u = conj_s
#     while(u != 0):
#         # S* in argmax{|Si|:Si in F}
#         c.append(conj_s*)
#         f.pop(s*)
#         u.pop(s*)
#         for sj in f:
#             #sj = sj - s*
#             if sj = 0:
#                 f.pop(sj)

    

