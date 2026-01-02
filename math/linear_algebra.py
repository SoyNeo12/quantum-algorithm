import numpy as np

def dagger(matrix):
    return matrix.conj().T

def tensor(a, b):
    return np.kron(a, b)