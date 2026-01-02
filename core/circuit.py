class QuantumCircuit:
    def __init__(self, initial_state):
        self.state = initial_state
        self.operations = []

    def apply_unitary(self, U, label=None):
        self.state.apply_unitary(U)
        if label:
            self.operations.append(label)

    def apply_channel(self, channel_fn, *args):
        self.state.rho = channel_fn(self.state.rho, *args)

    def get_state(self):
        return self.state.rho