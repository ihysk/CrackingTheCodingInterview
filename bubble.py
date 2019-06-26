def bubblesort(l):
    for i in range(len(l)-1, 0, -1):
        for low in range(i):
            if l[low] > l[low+1]:
                tmp = l[low]
                l[low] = l[low+1]
                l[low+1] = tmp
    return l


if __name__ == '__main__':
    from random import shuffle
    ll = list(range(0, 15))
    print(ll)
    shuffle(ll)
    print(ll)
    print(bubblesort(ll))
