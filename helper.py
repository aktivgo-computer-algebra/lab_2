from math import gcd as bltin_gcd


def is_mutually_simple(a, b: int) -> bool:
    return bltin_gcd(a, b) == 1
