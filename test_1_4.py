def is_permuration_of_palindrome(phrase):
    bitvec = create_bit_vector(phrase)
    return bitvec == 0 or check_onebit_set(bitvec)


def create_bit_vector(phrase):
    bitvec = 0
    for c in phrase:
        i = ord(c) - ord('a')
        bitvec ^= 1 << i
    return bitvec


def check_onebit_set(bitvec):
    return (bitvec & (bitvec - 1)) == 0


def test_1_4():
    assert is_permuration_of_palindrome('tactcoa')
