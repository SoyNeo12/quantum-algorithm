import numpy as np

def measure_z_basis(rho):
    P0 = np.array([[1, 0], [0, 0]], dtype=complex)
    P1 = np.array([[0, 0], [0, 1]], dtype=complex)

    p0 = np.real(np.trace(P0 @ rho))
    p1 = np.real(np.trace(P1 @ rho))

    return {
        "0": float(p0),
        "1": float(p1)
    }