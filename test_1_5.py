def one_edit_replace(str1, str2):
    found_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_diff:
                return False
            found_diff = True
    return True


# len(str2) > len(str1)
def one_edit_insert(str1, str2):
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index1 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def one_edit_away(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 == len2:
        return one_edit_replace(str1, str2)
    elif len1 + 1 == len2:
        return one_edit_insert(str2, str1)
    elif len1 == len2 + 1:
        return one_edit_insert(str1, str2)
    else:
        return False


def test_1_5():
    assert one_edit_away('pale', 'ple')
    assert one_edit_away('pales', 'pale')
    assert one_edit_away('pale', 'bale')
    assert one_edit_away('pale', 'bake') == False
