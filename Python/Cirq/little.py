import cirq

# Define a circuit using Cirq
qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit(cirq.X(qubit), cirq.measure(qubit))

# Run the circuit using the Cirq simulator
simulator = cirq.Simulator()
result = simulator.run(circuit)

# Print the measurement result
print(result)
