from projectq import *
from projectq.ops import C, BasicMathGate,H, Z, X, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.backends._sim._simulator import Simulator
from customgates import *
from probabilities_and_amplitudes import *

def s1(eng, qubits, R):
    A = qubits[5:8]
    output_reg = qubits[8:12]
    test_carrier_1 = qubits[12]
    test_carrier_2 = qubits[13]

    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])

    X | output_reg[0]
    X | test_carrier_1
    X | test_carrier_2

    MultiplyModN(2) | (A,R,output_reg)
    modular_decrement_gate() | (R,output_reg)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_1
    Uncompute(eng)

    modular_increment_gate() | (R,output_reg)
    modular_increment_gate() | (R,output_reg)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_2
    Uncompute(eng)

    C(Z,1) | (test_carrier_2,test_carrier_1)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_2
    Uncompute(eng)

    modular_decrement_gate() | (R,output_reg)
    modular_decrement_gate() | (R,output_reg)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_1
    Uncompute(eng)

    modular_increment_gate() | (R,output_reg)
    InverseMultiplyModN(2) | (A,R,output_reg)
    
    C(X,1) | (R[3], A[2])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[1], A[0])

    X | output_reg[0]
    X | test_carrier_1
    X | test_carrier_2
    
def s2(eng,qubits,R):
    
    A = qubits[5:7]
    output_reg = qubits[7:11]
    test_carrier_1 = qubits[11]
    test_carrier_2 = qubits[12]
    test_carrier_3 = qubits[13]

    X | output_reg[0]
    X | test_carrier_1
    X | test_carrier_2
    X | test_carrier_3

    C(X,1) | (R[2], A[0])
    C(X,1) | (R[3], A[1])
    
    MultiplyModN(2) | (A,R,output_reg)
    modular_decrement_gate() | (R,output_reg)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_1
    Uncompute(eng)
    
    modular_increment_gate() | (R,output_reg)
    modular_increment_gate() | (R,output_reg)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_2
    Uncompute(eng)

    modular_decrement_gate() | (R,output_reg)
    MultiplyModN(2) | (A,R,output_reg)
    
    modular_increment_gate() | (R,output_reg)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_3
    Uncompute(eng)
    
    C(Z,2) | (test_carrier_1,test_carrier_2,test_carrier_3)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_3
    Uncompute(eng)

    modular_decrement_gate() | (R, output_reg)
    InverseMultiplyModN(2) | (A,R,output_reg)
    modular_increment_gate() | (R,output_reg)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_2
    Uncompute(eng)

    modular_decrement_gate() | (R, output_reg)
    modular_decrement_gate() | (R, output_reg)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_1
    Uncompute(eng)

    modular_increment_gate() | (R, output_reg)

    InverseMultiplyModN(2) | (A,R,output_reg)
    
    X | output_reg[0]
    X | test_carrier_1
    X | test_carrier_2
    X | test_carrier_3
    C(X,1) | (R[3], A[1])
    C(X,1) | (R[2], A[0])

def s3(eng, qubits, R):
    A = qubits[5]
    output_reg = qubits[6:10]
    test_carrier_1 = qubits[10]
    test_carrier_2 = qubits[11]
    test_carrier_3 = qubits[12]
    test_carrier_4 = qubits[13]

    X | output_reg[0]
    X | test_carrier_1
    X | test_carrier_2
    X | test_carrier_3
    X | test_carrier_4

    C(X,1) | (R[3], A)

    MultiplyModN(2) | (A,R,output_reg)
    modular_decrement_gate()| (R, output_reg)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_1
    Uncompute(eng)

    modular_increment_gate() | (R, output_reg)
    modular_increment_gate() | (R, output_reg)

    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_2
    Uncompute(eng)

    MultiplyModN(2) | (A,R,output_reg)
    modular_increment_gate() | (R, output_reg)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_3
    Uncompute(eng)

    modular_decrement_gate() | (R,output_reg)
    MultiplyModN(4) | (A,R,output_reg)
    modular_increment_gate() | (R,output_reg)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_4
    Uncompute(eng)

    C(Z,3) | (test_carrier_1,test_carrier_2,test_carrier_3,test_carrier_4)
    
    with Compute(eng):
        All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_4
    Uncompute(eng)

    modular_decrement_gate() | (R,output_reg)
    InverseMultiplyModN(4) | (A,R,output_reg)
    modular_increment_gate() | (R,output_reg)
    
    with Compute(eng):
           All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_3
    Uncompute(eng)

    modular_decrement_gate() | (R,output_reg)
    InverseMultiplyModN(2) | (A,R,output_reg)

    with Compute(eng):
           All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_2
    Uncompute(eng)

    modular_decrement_gate() | (R,output_reg)
    modular_decrement_gate() | (R,output_reg)

    with Compute(eng):
           All(X) | output_reg
    with Control(eng, output_reg):
        X | test_carrier_1
    Uncompute(eng)

    modular_increment_gate() | (R,output_reg)
    InverseMultiplyModN(2) | (A,R,output_reg)
    
    C(X,1) | (R[3], A)

    X | output_reg[0]
    X | test_carrier_1
    X | test_carrier_2
    X | test_carrier_3
    X | test_carrier_4
    
eng = MainEngine()
qubits = eng.allocate_qureg(14)
control_qubit = qubits[0]
R = qubits[1:5]

All(X) | R[0:4]
All(H) | R[0:4]
###
C(X,2) | (R[0:2],control_qubit)
with Control(eng,control_qubit):
    s1(eng, qubits,R)
C(X,2) | (R[0:2],control_qubit)
####
X | R[1]
C(X,3) | (R[0:3], control_qubit)
X | R[1]

with Control(eng,control_qubit):
    s2(eng, qubits,R)
    
X | R[1]
C(X,3) | (R[0:3], control_qubit)
X | R[1]

####
All(X) | R[1:3]
C(X,3) | (R[0:3],control_qubit)
All(X) | R[1:3]

with Control(eng,control_qubit):
    s3(eng, qubits,R)

All(X) | R[1:3]
C(X,3) | (R[0:3],control_qubit)
All(X) | R[1:3]
####
Z | R[0]
All(H) | R[0:4]
C(Z,3) | (R[0:3],R[3])
All(H) | R[0:4]
eng.flush()
print(get_all_probabilities(eng,R))
print(get_all_probabilities(eng,qubits))
print(get_all_amplitudes(eng,qubits))

Measure | qubits
