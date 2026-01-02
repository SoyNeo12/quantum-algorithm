from api.simulator import simulate_noisy_hadamard

if __name__ == "__main__":
    result = simulate_noisy_hadamard(noise_level=0.2)
    print("Measurement probabilities:")
    print(result)