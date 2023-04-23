import numpy as np

def minimum_set_cover(matriz, k):
    n = matriz.shape[0]
    m = matriz.shape[1]

    selected_sets = []

    while len(selected_sets) < k:
        uncovered_elements = set(range(m))
        max_covered = -1
        max_set_idx = -1

        for i in range(n):
            covered_elements = uncovered_elements.intersection(set(np.where(matriz[i] == 1)[0]))
            if len(covered_elements) > max_covered:
                max_covered = len(covered_elements)
                max_set_idx = i

        selected_sets.append(max_set_idx)

        uncovered_elements = uncovered_elements.difference(set(np.where(matriz[max_set_idx] == 1)[0]))

        matriz[max_set_idx] = np.zeros(m)

    return selected_sets
