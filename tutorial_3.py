from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
from math import pi
import matplotlib.pyplot as plt
from qiskit_aer import Aer

circuit = QuantumCircuit(4)
circuit.x([0,2,3])
# circuit.y(0)
circuit.draw(output='mpl')

# simulator = Aer.get_backend('qasm_simulator')
# result = execute(circuit, backend = simulator, shots=102400).result()
# plot_histogram(result.get_counts())
# plt.show()

simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
state_vector = result.get_statevector()
plot_bloch_multivector(state_vector)
plt.show()