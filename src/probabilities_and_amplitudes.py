from projectq.backends._sim._simulator import Simulator

def get_all_probabilities(eng,qureg):
    i = 0
    y = len(qureg)
    while i < (2**y):
       qubit_list = [int(x) for x in list(('{0:0b}'.format(i)).zfill(y))]
       qubit_list = qubit_list[::-1]
       l = eng.backend.get_probability(qubit_list,qureg)
       if l != 0.0:
#           qubit_list[::-1]
           print(l,qubit_list, i)
       i += 1

def get_all_amplitudes(eng,qureg):
    i = 0
    y = len(qureg)
    while i < (2**y):
       qubit_list = [int(x) for x in list(('{0:0b}'.format(i)).zfill(y))]
       l = eng.backend.get_amplitude(qubit_list,qureg)
       if l != 0.0:
           print(l,qubit_list, i)
       i += 1

