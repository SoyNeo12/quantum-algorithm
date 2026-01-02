from core.state import DensityMatrix
from core.circuit import QuantumCircuit
from core.operators import H
from core.channels import depolarizing_channel
from core.measurement import measure_z_basis

def simulate_noisy_hadamard(noise_level=0.1):
    initial = DensityMatrix.pure_state([1, 0])
    circuit = QuantumCircuit(initial)

    circuit.apply_unitary(H, label="H")
    circuit.apply_channel(depolarizing_channel, noise_level)

    probabilities = measure_z_basis(circuit.get_state())
    return probabilities