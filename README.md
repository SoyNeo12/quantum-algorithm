# Quantum Circuit Simulator with Noise Modeling

A rigorous quantum circuit simulator based on the density matrix formalism, designed to model open quantum systems and noise effects using mathematically correct quantum channels.

This project focuses on correctness, clarity, and extensibility rather than convenience abstractions. It implements core concepts from quantum information theory and linear algebra with explicit validation and minimal dependencies.

## Motivation

Most introductory quantum simulators rely exclusively on pure state vectors and idealized unitary evolution. While useful for learning, such models fail to capture realistic quantum behavior observed in physical systems.

This simulator adopts the density matrix formalism, enabling the representation of mixed states, decoherence, and noise through Completely Positive Trace-Preserving (CPTP) maps. The goal is to provide a foundation suitable for both educational and research-oriented experimentation.

## Core Principles

- Explicit mathematical correctness over abstraction
- Separation between mathematical validation, physical modeling, and execution logic
- No reliance on external quantum frameworks
- Deterministic, reproducible simulations
- Readable and extensible architecture

## Implemented Concepts

- Density matrices for quantum state representation
- Unitary evolution via matrix conjugation
- Quantum measurements using projection operators
- Noise and decoherence via Kraus operator channels
- Trace preservation and positivity validation
- Open quantum system modeling

## Features

- Pure and mixed quantum state support
- Hermiticity, trace, and positivity checks on all states
- Unitary operators (Hadamard, Pauli operators)
- Quantum noise channels:
  - Depolarizing channel
  - Amplitude damping channel
- Circuit execution engine with ordered operations
- Deterministic example simulations

## Project Structure

```
quantum-simulator/
│
├── core/
│ ├── state.py # Density matrix representation
│ ├── operators.py # Unitary operators and observables
│ ├── channels.py # Noise and decoherence models (CPTP maps)
│ ├── circuit.py # Circuit execution engine
│ └── measurement.py # Measurement operators
│
├── math/
│ ├── linear_algebra.py
│ └── validation.py # Physical and mathematical validation
│
├── api/
│ └── simulator.py # High-level simulation interface
│
├── examples/
│ └── noisy_hadamard.py
│
└── main.py
```

## Example

The following simulation applies a Hadamard gate to an initial |0⟩ state and then introduces depolarizing noise:

```python
from api.simulator import simulate_noisy_hadamard

result = simulate_noisy_hadamard(noise_level=0.2)
print(result)
```

Output (example):

```
{'0': 0.50, '1': 0.50}
```

As noise increases, the system converges toward the maximally mixed state.

## Design Notes

- All quantum states are validated for:
  - Hermiticity
  - Unit trace
  - Positive semidefiniteness

- Noise channels are implemented explicitly via Kraus representations
- No implicit state mutation outside controlled execution paths
- Matrix operations are expressed directly for transparency

## Limitations

- Currently supports single-qubit systems only
- No performance optimizations for large Hilbert spaces
- Classical simulation only (no hardware backends)

These constraints are intentional to maintain clarity and correctness.

## Roadmap

- Multi-qubit support via tensor products
- Additional noise models (phase damping, generalized amplitude damping)
- Expectation value computation for arbitrary observables
- Bloch sphere visualization
- Benchmark comparisons with analytical results

## Disclaimer

This project is a classical simulation of quantum mechanics intended for educational, analytical, and experimental purposes. It does not interface with physical quantum hardware.

## Author

Developed by **SoyNeo12**

## License

MIT
