def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if l[min] > l[j]:
                min = j

        tmp = l[i]
        l[i] = l[min]
        l[min] = tmp

    return l


if __name__ == '__main__':
    from random import shuffle
    ll = list(range(0, 15))
    print(ll)
    shuffle(ll)
    print(ll)
    print(selection_sort(ll))
