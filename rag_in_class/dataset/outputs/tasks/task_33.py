def decimal_To_Binary(N):
    binary_number = 0
    counter = 0
    while N != 0:
        remainder = N % 2
        power = pow(10, counter)
        binary_number += remainder * power
        N = N // 2
        counter += 1
    return binary_number
