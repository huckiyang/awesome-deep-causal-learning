import numpy as np
import pickle

from qiskit import IBMQ, transpile, QuantumCircuit
from qiskit.providers.ibmq.managed import IBMQJobManager
from qiskit.circuit import Parameter
from qiskit.circuit.random import random_circuit


with open("ibmq_bogota_noise" + ".txt", "rb") as fp:
	device_properties_bogota = pickle.load(fp)



with open("ibmq_rome_noise" + ".txt", "rb") as fp:
	device_properties_rome = pickle.load(fp)



print(device_properties_bogota)

print(device_properties_rome)