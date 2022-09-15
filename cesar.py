import math

import helper


def validate(alphabet: [str], a: int):
    if a == 0:
        raise Exception("a is equal 0")
    if not helper.is_mutually_simple(len(alphabet), a):
        raise Exception("|A| and 'a' not are mutually simple")


class Cesar:
    alphabet = [str]

    a = 0
    b = 0

    permutation = [str]

    def __init__(self, alphabet: [str], a, b: int, permutation: [str]):
        self.alphabet = alphabet
        self.a = a
        self.b = b
        self.permutation = permutation

        validate(alphabet, a)

    def encode_by_formula(self, message: str) -> str:
        result = ""
        for s in message:
            result += self.alphabet[(self.a * self.alphabet.index(s) + self.b) % len(self.alphabet)]
        return result

    def encode_by_permutation(self, message: str) -> str:
        result = ""
        for s in message:
            result += self.permutation[self.alphabet.index(s)]
        return result

    def decode_by_formula(self, message: str) -> str:
        result = ""
        inverse_a = helper.get_inverse_number_in_ring_modulo(self.a, len(self.alphabet))
        for s in message:
            result += self.alphabet[
                inverse_a * (self.alphabet.index(s) - self.b) % len(self.alphabet)
            ]
        return result

    def decode_by_permutation(self, message: str) -> str:
        result = ""
        for s in message:
            result += self.alphabet[self.permutation.index(s)]
        return result
