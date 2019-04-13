def replace_spaces(text, true_len):
    space_cnt = 0
    for i in range(true_len):
        if text[i] == ' ':
            space_cnt += 1

    index = true_len + space_cnt * 3
    phrase = [''] * index
    for i in reversed(range(true_len)):
        if text[i] == ' ':
            phrase[index - 1] = '0'
            phrase[index - 2] = '2'
            phrase[index - 3] = '%'
            index -= 3
        else:
            phrase[index - 1] = text[i]
            index -= 1
    return ''.join(phrase)


def test_1_3():
    phrase = 'hoge hoge hoge'
    print(replace_spaces(phrase, 14))
