from math import gcd as bltin_gcd


def is_mutually_simple(a, b: int) -> bool:
    return bltin_gcd(a, b) == 1


def get_inverse_number_in_ring_modulo(a, module: int) -> int:
    if not is_mutually_simple(a, module):
        raise Exception("'a' and module are not mutually simple")

    result = 1

    while a * result % module != 1:
        result += 1

    return result
