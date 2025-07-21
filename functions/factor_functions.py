import numpy as np

def get_factors(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError('Input n must be non-negative integer')

    factors = []
    for i in range(1, int(np.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return np.sort(factors)

def is_prime(n):
    return len(get_factors(n)) == 2