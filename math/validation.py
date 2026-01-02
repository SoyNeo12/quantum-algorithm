import numpy as np

def validate_density_matrix(rho):
    if rho.shape[0] != rho.shape[1]:
        raise ValueError("Density matrix must be square.")

    if not np.allclose(rho, rho.conj().T):
        raise ValueError("Density matrix must be Hermitian.")

    trace = np.trace(rho)
    if not np.isclose(trace, 1.0):
        raise ValueError("Trace of density matrix must be 1.")

    eigenvalues = np.linalg.eigvals(rho)
    if any(ev < -1e-10 for ev in eigenvalues):
        raise ValueError("Density matrix must be positive semidefinite.")