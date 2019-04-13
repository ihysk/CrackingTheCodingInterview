def permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    table = [0] * 128
    for c in str1:
        i = ord(c)
        table[i] += 1

    for c in str2:
        i = ord(c)
        table[i] -= 1
        if table[i] < 0:
            return False
    return True


def test_1_2():
    assert permutation('dog', 'god')
    assert permutation('hoge', 'ogeh')
    assert permutation('Dog', 'dog') == False

    assert permutation2('dog', 'god')
    assert permutation2('hoge', 'ogeh')
    assert permutation2('Dog', 'dog') == False
