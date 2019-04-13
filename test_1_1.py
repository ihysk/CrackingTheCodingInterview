a_len = 128


def is_unique_chars(str):
    if len(str) > a_len:
        return False

    # Ascii 128個分の配列
    char_set = [False] * a_len
    for c in str:
        ac = ord(c)
        if char_set[ac]:
            return False
        char_set[ac] = True
    return True


def is_unique_chars2(str):
    # 仮にcheckerをintのビットベクトルとする
    checker = 0
    for c in str:
        i = ord(c) - ord('a')
        if checker & 1 << i:
            return False
        checker ^= 1 << i
    return True


def is_unique_chars3(str):
    for i, c in enumerate(str):
        for i2 in range(i+1, len(str)):
            if c == str[i2]:
                return False
    return True


def test_1_1():
    assert is_unique_chars('hoge') == True
    assert is_unique_chars('hogehoge') == False
    assert is_unique_chars('abcdefg')

    assert is_unique_chars2('hoge') == True
    assert is_unique_chars2('hogehoge') == False
    assert is_unique_chars2('abcdefg')

    assert is_unique_chars3('hoge') == True
    assert is_unique_chars3('hogehoge') == False
    assert is_unique_chars3('abcdefg')
