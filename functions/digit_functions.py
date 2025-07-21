import numpy as np

def get_digits(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError('Input n must be non-negative integer')
        
    digits = np.array([int(d) for d in str(n)])
    return digits

def get_digit(n, i):
    return get_digits(n)[i-1]

def num_digits(n):
    return len(get_digits(n))

def is_unique_digits(n):
    digits = get_digits(n)
    return len(np.unique(digits)) == len(digits)

def num_reverse(n):
    digits = get_digits(n)[::1]
    digits.reverse()
    return int(''.join(str(d) for d in digits))

def digit_sum(n):
    digits = get_digits(n)
    return np.sum(digits)

def digit_product(n):
    digits = get_digits(n)
    return np.prod(digits)