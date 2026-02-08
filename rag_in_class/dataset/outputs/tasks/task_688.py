import cmath

def len_complex(a, b):
    if isinstance(a, complex) or isinstance(b, complex):
        cn = complex(a, b)
    else:
        cn = complex(a, b)
    length = abs(cn)
    return length
