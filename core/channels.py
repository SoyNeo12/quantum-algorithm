import numpy as np
from math.validation import validate_density_matrix

def depolarizing_channel(rho, p):
    I = np.eye(rho.shape[0], dtype=complex)
    noisy_rho = (1 - p) * rho + p * I / rho.shape[0]
    validate_density_matrix(noisy_rho)
    return noisy_rho


def amplitude_damping_channel(rho, gamma):
    E0 = np.array([
        [1, 0],
        [0, np.sqrt(1 - gamma)]
    ], dtype=complex)

    E1 = np.array([
        [0, np.sqrt(gamma)],
        [0, 0]
    ], dtype=complex)

    new_rho = (
        E0 @ rho @ E0.conj().T +
        E1 @ rho @ E1.conj().T
    )

    validate_density_matrix(new_rho)
    return new_rho