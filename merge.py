def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])

    return merged


if __name__ == '__main__':
    from random import shuffle
    ll = list(range(0, 15))
    print(ll)
    shuffle(ll)
    print(ll)
    print(merge_sort(ll))
