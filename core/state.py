import numpy as np
from math.validation import validate_density_matrix

class DensityMatrix:
    def __init__(self, rho: np.ndarray):
        self.rho = np.array(rho, dtype=complex)
        validate_density_matrix(self.rho)

    @classmethod
    def pure_state(cls, state_vector):
        state_vector = np.array(state_vector, dtype=complex).reshape(-1, 1)
        rho = state_vector @ state_vector.conj().T
        return cls(rho)

    def apply_unitary(self, U):
        self.rho = U @ self.rho @ U.conj().T
        validate_density_matrix(self.rho)