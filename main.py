import numpy as np
from typing import Optional


def multiply_matrices(m1: np.ndarray, m2: np.ndarray) -> Optional[np.ndarray]:
    if m1.ndim != 2 or m2.ndim != 2 or m1.shape[1] != m2.shape[0]:
        return None
    ret = np.zeros((m1.shape[0], m2.shape[1]), dtype=np.longdouble)
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            for k in range(m2.shape[0]):
                ret[i][j] += m1[i][k] * m2[k][j]
    return ret


mat_1 = np.array([[1, 3, 5, 2], [8, 2, 1, 5]])
mat_2 = np.array([[42], [41], [92], [3]])

print(multiply_matrices(mat_1, mat_2))
