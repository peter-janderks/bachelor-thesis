from projectq import *
from projectq.ops import C, BasicMathGate,H, Z, X, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.backends._sim._simulator import Simulator
from customgates import *

def test_MultiplyModN():
    ### 4 qubits, s=1 --> len(A) = 3 
    eng = MainEngine()
    R = eng.allocate_qureg(4)
    A = eng.allocate_qureg(3)
    output_reg = eng.allocate_qureg(4)
    All(X) | R[0:3]
    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])
    X | output_reg[0]
    MultiplyModN(2) | (A,R,output_reg)
    eng.flush()
    Measure | R
    Measure | A
    Measure | output_reg
    
    assert [int(qubit) for qubit in R] == [1,1,1,0]
    assert [int(qubit) for qubit in A] == [1,1,0]
    assert [int(qubit) for qubit in output_reg] == [1,0,0,0]

    ### 4 qubits, s=1 --> len(A) = 3                                                      
    eng = MainEngine()
    R = eng.allocate_qureg(4)
    A = eng.allocate_qureg(3)
    output_reg = eng.allocate_qureg(4)
    All(X) | R[0:3]
    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])
    X | output_reg[0]
    MultiplyModN(2) | (A,R,output_reg)
    X | output_reg[0]
    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])
    All(X) | R[0:3]
    eng.flush()
    Measure | R
    Measure | A
    Measure | output_reg

    print([int(qubit) for qubit in R],'register R')
    print([int(qubit) for qubit in A],'register A')
    print([int(qubit) for qubit in output_reg],'output_reg')

    ### n=5 qubits, s=1 -->len(a) = 4
    ### http://algassert.com/quirk#circuit={%22cols%22:[[%22X%22,%22X%22,%22X%22,%22X%22,%22X%22,1,1,1,1,%22X%22,%22setB%22],[1,%22inputA4%22,1,1,1,%22+=A4%22],[%22inputR5%22,1,1,1,1,%22inputA4%22,1,1,1,%22*BToAmodR5%22],[1,1,1,1,1,1,1,1,1,%22Chance5%22]]}
    ### 2^15 mod 31 = 1
    eng = MainEngine()
    R = eng.allocate_qureg(5)
    A = eng.allocate_qureg(4)
    output_reg = eng.allocate_qureg(5)
    All(X) | R
    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])
    C(X,1) | (R[4], A[3])
    X | output_reg[0]
    MultiplyModN(2) | (A,R,output_reg)
    eng.flush()
    Measure | R
    Measure | A
    Measure | output_reg
    assert [int(qubit) for qubit in R] == [1,1,1,1,1]
    assert [int(qubit) for qubit in A] == [1,1,1,1]
    assert [int(qubit) for qubit in output_reg] == [1,0,0,0,0]

    # N = 6 qubits, s=1 --> len(a) = 5 (Too big for quirk!) 2^31 mod 63 = 2 
    eng = MainEngine()
    R = eng.allocate_qureg(6)
    A = eng.allocate_qureg(5)
    output_reg = eng.allocate_qureg(6)
    All(X) | R
    C(All(X),5) | (R[1:6], A[0:5])
    X | output_reg[0]
    MultiplyModN(2) | (A,R,output_reg)
    eng.flush()
    Measure | R
    Measure | A
    Measure | output_reg
    assert [int(qubit) for qubit in R] == [1,1,1,1,1,1]
    assert [int(qubit) for qubit in A] == [1,1,1,1,1]
    assert [int(qubit) for qubit in output_reg] == [0,1,0,0,0,0]

def test_InverseMultiplyModN():
    ### 4 qubits, s=1 --> len(A) = 3                                            
    eng = MainEngine()
    R = eng.allocate_qureg(4)
    A = eng.allocate_qureg(3)
    output_reg = eng.allocate_qureg(4)
    All(X) | R[0:4]
    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])
    All(X) | output_reg[0:3]
    InverseMultiplyModN(2) | (A,R,output_reg)
    C(X,1) | (R[1], A[0])
    C(X,1) | (R[2], A[1])
    C(X,1) | (R[3], A[2])
    All(X) | R[0:4]
    eng.flush()
    Measure | R
    Measure | A
    Measure | output_reg


def test_modular_increment_gate():
    print('hi')
    eng = MainEngine()
    R = eng.allocate_qureg(4)
    output_reg = eng.allocate_qureg(4)
    All(X) | R
    X | output_reg[0]
    modular_increment_gate() | (R,output_reg)
    eng.flush()
    Measure | output_reg
    assert [int(qubit) for qubit in output_reg] == [0,1,0,0]
    
    eng = MainEngine()
    R = eng.allocate_qureg(4)
    output_reg = eng.allocate_qureg(4)
    All(H) | R[0:3]
    All(X) | output_reg[0:3]
    modular_increment_gate() | (R,output_reg)
    eng.flush()
    Measure | R
    Measure | output_reg
    assert [int(qubit) for qubit in output_reg] == [1,1,1,0]

def test_modular_decrement_gate():
    eng = MainEngine()
    R = eng.allocate_qureg(4)
    output_reg = eng.allocate_qureg(4)
    All(X) | R
    X | output_reg[0]
    modular_decrement_gate() | (R,output_reg)
    eng.flush()
    Measure | output_reg
    assert [int(qubit) for qubit in output_reg] == [0,0,0,0]

    eng = MainEngine()
    R = eng.allocate_qureg(4)
    output_reg = eng.allocate_qureg(4)
    All(H) | R[0:3]
    All(X) | output_reg[0:3]
    modular_decrement_gate() | (R,output_reg)
    eng.flush()
    Measure | R
    Measure | output_reg
    assert [int(qubit) for qubit in output_reg] == [1,1,1,0]

test_MultiplyModN()
test_InverseMultiplyModN()
test_modular_increment_gate()
test_modular_decrement_gate()

