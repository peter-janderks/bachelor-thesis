base = 2

def extended_gcd(a, b):
    lastremainder, remainder = abs(a), abs(b)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if a < 0 else 1), lasty * (-1 if b < 0 else 1)


def find_inverse(value, modulus):
    (gcd, x ,y) = extended_gcd(value, modulus)
    if gcd != 1:
        print('no')
        return 'undefined'
    print(x,gcd)
    return x % modulus

def mod(exponent,modulus,val):
    if modulus == 0 or val >= modulus:
        print('if')
        return (exponent,modulus,val)
    else:
        inverse = find_inverse(base,modulus)
        print(inverse,'inverse')
        
        if inverse == 'undefined':
            return(exponent,modulus,val)
        exp = exponent
        while (exp > 0):
            print('yes')
            if ((exp & 1) != 0):
                val = (val * inverse) % modulus
            inverse = (inverse * inverse) % modulus
            exp >>= 1
        return(exponent,modulus,val)


print(mod(3,7,15))
