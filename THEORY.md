# Theoretical Background

This document outlines the mathematical and physical foundations underlying the quantum circuit simulator. The simulator is based on the formalism of density matrices and open quantum systems, ensuring correctness beyond idealized pure-state models.

## 1. Quantum States

### 1.1 Pure States

A pure quantum state is represented by a normalized vector |ψ⟩ in a complex Hilbert space ℋ:

|ψ⟩ ∈ ℂⁿ, ⟨ψ|ψ⟩ = 1

In the computational basis for a single qubit:

|ψ⟩ = α|0⟩ + β|1⟩, α, β ∈ ℂ

Pure states provide a complete description only for isolated quantum systems. They are insufficient to represent statistical mixtures or interactions with an environment.

### 1.2 Density Matrices

To represent general quantum states, including mixed states, the simulator uses the density matrix formalism.

A density matrix ρ is defined as:

ρ = Σᵢ pᵢ |ψᵢ⟩⟨ψᵢ|

where:

- pᵢ ≥ 0
- Σᵢ pᵢ = 1

A matrix ρ represents a physically valid quantum state if and only if it satisfies:

1. Hermiticity: ρ = ρ†
2. Unit trace: Tr(ρ) = 1
3. Positivity: ρ ≥ 0 (positive semidefinite)

All states generated and transformed within the simulator are explicitly validated against these conditions.

## 2. Quantum Evolution

### 2.1 Unitary Evolution

For closed quantum systems, time evolution is governed by unitary operators U:

ρ → U ρ U†

Unitary evolution preserves the defining properties of a density matrix, namely Hermiticity, trace, and positivity.

In this simulator, quantum gates such as the Hadamard and Pauli operators are implemented directly as unitary matrices acting via conjugation.

### 2.2 Open Quantum Systems

Realistic quantum systems are rarely isolated and typically interact with an external environment. Such systems are referred to as open quantum systems.

The evolution of open quantum systems cannot, in general, be described by unitary operators alone. Instead, the most general physically admissible evolution is described by Completely Positive Trace-Preserving (CPTP) maps.

## 3. Quantum Channels and Noise

### 3.1 Kraus Representation

Any CPTP map ℰ acting on a density matrix ρ admits a Kraus representation of the form:

ℰ(ρ) = Σₖ Eₖ ρ Eₖ†

where the Kraus operators {Eₖ} satisfy the completeness condition:

Σₖ Eₖ† Eₖ = I

This condition guarantees that the evolution preserves the trace of the density matrix and remains physically valid even when extended to larger composite systems.

### 3.2 Depolarizing Channel

The depolarizing channel models uniform, basis-independent noise that drives the system toward the maximally mixed state:

ℰ(ρ) = (1 − p) ρ + p (I / d)

where:

- p ∈ [0, 1] is the noise strength
- d is the dimension of the Hilbert space

As p approaches 1, all information about the initial state is lost and the system converges to complete classical uncertainty.

### 3.3 Amplitude Damping Channel

The amplitude damping channel models irreversible energy loss processes, such as spontaneous emission.

It is defined by the following Kraus operators:

E₀ = [[1, 0], [0, √(1 − γ)]]

E₁ = [[0, √γ], [0, 0]]

where γ ∈ [0, 1] represents the damping rate. This channel captures both decoherence and population decay effects.

## 4. Measurement

Quantum measurement is modeled using projection operators. For a measurement in the computational (Z) basis, the projectors are:

P₀ = |0⟩⟨0|  
P₁ = |1⟩⟨1|

The probability of obtaining outcome i is given by the Born rule:

p(i) = Tr(Pᵢ ρ)

Measurement outcomes in the simulator are computed directly using this formalism.

## 5. Scope and Limitations

The simulator focuses on mathematical correctness and conceptual clarity rather than performance or scalability.

Current limitations include:

- Single-qubit systems only
- No time-continuous dynamics
- No hardware backends

These constraints are intentional and serve to maintain a transparent and verifiable implementation.

## 6. Summary

By adopting the density matrix formalism and CPTP quantum channels, this simulator provides a rigorous foundation for modeling realistic quantum systems. The architecture reflects the structure of modern quantum information theory while remaining accessible for analysis and extension.
