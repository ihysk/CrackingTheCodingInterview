def compress_bad(str):
    compressed_str = ''
    count = 0
    for i in range(len(str)):
        count += 1
        print(i, len(str))
        if len(str) - 1 == i or str[i + 1] != str[i]:
            compressed_str += f'{str[i]}{count}'
            count = 0
    return compressed_str if len(compressed_str) < len(str) else str


def test_1_6():
    assert compress_bad('aabccccaaa') == 'a2b1c4a3'
    assert compress_bad('abcde') == 'abcde'
    assert compress_bad('bbbbcccccabab') == 'b4c5a1b1a1b1'
