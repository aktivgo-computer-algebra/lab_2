import cesar
import vigenor
import string

if __name__ == '__main__':
    alphabet = string.ascii_lowercase
    print("alphabet:", alphabet)

    a = int(input("input a: "))
    b = int(input("input b: "))

    permutation = string.ascii_uppercase

    cesar = cesar.Cesar(alphabet, a, b, permutation)

    message = input("input message: ")

    encoded_cesar_formula = cesar.encode_by_formula(message)
    print("cesar encode by formula:", encoded_cesar_formula)

    print("permutation:", permutation)

    encoded_cesar_permutation = cesar.encode_by_permutation(message)
    print("cesar encode by permutation:", encoded_cesar_permutation)

    print("cesar decode by formula:", cesar.decode_by_formula(encoded_cesar_formula))
    print("cesar decode by permutation:", cesar.decode_by_permutation(encoded_cesar_permutation))

    permutations = [
        string.ascii_uppercase,
        string.ascii_lowercase
    ]

    print("permutation set:", permutations)

    vigenor = vigenor.Vigenor(alphabet, permutations)

    encoded_vigenor = vigenor.encode(message)
    print("vigenor encode:", encoded_vigenor)
    print("vigenor decode:", vigenor.decode(encoded_vigenor))



