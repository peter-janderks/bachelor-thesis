from projectq import *
from projectq.ops import C, BasicMathGate,H, Z, X, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.backends._sim._simulator import Simulator

class MultiplyModN(BasicMathGate):
    """
    Takes three quantum registers as input, 'exponent, 'modulus' and 'val'.
    The gate returns the exponent and modulus registers unchanged, and
    multiplies the val register by base^exponent mod(modulus)
    The numbers in quantum registers are stored from low- to high-bit, i.e., 
    qunum[0] is the LSB.
    """
    def __init__(self, a):
        """
        Initializes the gate to the base to be used for modular 
        exponentiation.
        Args:
            base (int): base for the modular exponentiation.  
        It also initializes its base class, BasicMathGate, with the
        corresponding function, so it can be emulated efficiently.
        
        Example:
            .. code-block:: python
            MultiplyModN(2) | (qureg1, qureg2, qureg3)
        """
        def mod(exponent,modulus,val):
            # does not change the val if it is bigger than the modulus (this 
            # would be irreversible) or if the modulus = 0 (division by 0 not 
            # possible)
            if modulus == 0 or val >= modulus:
               return (exponent,modulus,val)
            
            else:
                 # repeated squaring algorithm    
                base = a
                exp = exponent               
                while (exp > 0):
                    # if exp is odd, multiply inverse with val
                    if ((exp & 1) != 0):
                        val = (val * base) % modulus
                    # square the base 
                    base = (base * base) % modulus
                    # binary shift 
                    exp >>= 1
                return(exponent,modulus,val)
        BasicMathGate.__init__(self,mod)
        self.a = a

class InverseMultiplyModN(BasicMathGate):
    """
    Takes three quantum registers as input, 'exponent, 'modulus' and 'val'.
    The gate returns the exponent and modulus registers unchanged, and
    multiplies the val register by inverse^exponent mod(modulus). 'Inverse' 
    is the modular multiplicative inverse of 'base'.
    The numbers in quantum registers are stored from low- to high-bit, i.e.,
    qunum[0] is the LSB.                                                                         
    """
    def __init__(self, a):
        """
        Initializes the gate to the base of which the inverse needs to be found
        Args:
            base (int): base of which the inverse needs to be found for modular 
                        multiplication
        It also initializes its base class, BasicMathGate, with the
        corresponding function, so it can be emulated efficiently.
        """
        def extended_gcd(a, b):
            # calculates the gcd and the coefficients of Bezout's identity
            lastremainder, remainder = abs(a), abs(b)
            x, lastx, y, lasty = 0, 1, 1, 0
            while remainder != 0:
                lastremainder, (quotient, remainder) = remainder, divmod(lastremainder,remainder)
                x, lastx = lastx - quotient*x, x
                y, lasty = lasty - quotient*y, y
            return lastremainder, lastx, lasty

        def find_inverse(value, mod):
            # if the gcd is not equal to one, the value does not have an inverse. 
            # if it is, the inverse is the first Bezout coefficient modulus mod
            (gcd, x ,y) = extended_gcd(value, mod)
            if gcd != 1:
               return 'undefined'
            return x % mod

        def mod(exponent,modulus,val):
            # does not change the val if it is bigger than the modulus (this
            # would be irreversible) or if the modulus = 0 (division by 0 not
            # possible)  
            base = a
            if exponent == 0 or modulus == 0 or val >= modulus:
                return (exponent,modulus,val)
            else:
                base = base
                inverse = find_inverse(base,modulus)
                
                if inverse == 'undefined':
                    return(exponent,modulus,val)
                exp = exponent

                while (exp > 0):
                    # if exp is odd, multiply inverse with val
                    if ((exp & 1) != 0):
                        val = (val * inverse) % modulus
                    # square the inverse (base)
                    inverse = (inverse * inverse) % modulus
                    # binary shift
                    exp >>= 1
                return(exponent,modulus,val)            
        BasicMathGate.__init__(self,mod)
        self.a = a

class modular_increment_gate(BasicMathGate):
    """
    Multiply a quantum number represented by a quantum register by a^b modulo N.
    The number is stored from low- to high-bit, i.e., qunum[0] is the LSB.
    """
    def __init__(self):
        """
        Initializes the gate to the number to multiply with modulo N.
        Args:
            a (int): Number by which to multiply a quantum register
                (0 <= a < N).
            N (int): Number modulo which the multiplication is carried out.
        It also initializes its base class, BasicMathGate, with the
        corresponding function, so it can be emulated efficiently.
        """
        def mod(N,x):
            if  N == 0 or x >= N:
                return(N,x)
            else:
                if x+1 == N:
                    return(N,0)
                else:
                    return(N,x+1)
        BasicMathGate.__init__(self,mod)

class modular_decrement_gate(BasicMathGate):
    """
    Multiply a quantum number represented by a quantum register by a^b modulo N.
    The number is stored from low- to high-bit, i.e., qunum[0] is the LSB.
    """
    def __init__(self):
        """
        Initializes the gate to the number to multiply with modulo N.
        Args:
            a (int): Number by which to multiply a quantum register
                (0 <= a < N).
            N (int): Number modulo which the multiplication is carried out.
        It also initializes its base class, BasicMathGate, with the
        corresponding function, so it can be emulated efficiently.
        """
        def mod(N,x):
            if  N == 0 or x >= N:
                return(N,x)
            if x == 0:
                return(N,N-1)
            else:
                return(N,x-1)
        BasicMathGate.__init__(self,mod)





