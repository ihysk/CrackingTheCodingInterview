def count_num_char(phrase):
    dic = {}
    for c in phrase:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic


def check_dic(dic):
    odd_cnt = 0
    for val in dic.values():
        if val % 2 == 1:
            odd_cnt += 1
    return odd_cnt


def is_permutation_of_palindrome(phrase):
    dic = count_num_char(phrase)
    cnt = check_dic(dic)
    return (cnt == 0 and len(phrase) % 2 == 0) or (cnt == 1 and len(phrase) % 2 == 1)


def test_1_4():
    assert is_permutation_of_palindrome('tactcoa')
