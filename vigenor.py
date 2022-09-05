class Vigenor:
    alphabet = [str]

    permutations = [[str]]

    def __init__(self, alphabet: [str], permutations: [[str]]):
        self.alphabet = alphabet
        self.permutations = permutations

    def encode(self, message: str) -> str:
        result = ""
        for i in range(0, len(message) - 1):
            result += self.permutations[i % len(self.permutations)][self.alphabet.index(message[i])]

        return result

    def decode(self, message: str) -> str:
        result = ""
        for i in range(0, len(message) - 1):
            result += self.permutations[i % len(self.permutations)][self.alphabet.index(message[i])]
        return result