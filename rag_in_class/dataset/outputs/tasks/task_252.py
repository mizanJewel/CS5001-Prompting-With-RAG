import cmath

def convert(numbers):
    if isinstance(numbers, complex):
        return numbers
    num = cmath.polar(numbers)
    return num
