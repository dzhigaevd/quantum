from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt
from qiskit_aer import Aer


qr = QuantumRegister(1)
cr = ClassicalRegister(1)

circuit = QuantumCircuit(qr,cr)
# circuit.h(qr)
# circuit.measure(qr, cr)

print(cr)

# simulator = Aer.get_backend('qasm_simulator')
# result = execute(circuit, backend = simulator, shots=102400).result()
# plot_histogram(result.get_counts())
# plt.show()

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator, shots=1).result()
state_vector = result.get_statevector()
plot_bloch_multivector(state_vector)
plt.show()