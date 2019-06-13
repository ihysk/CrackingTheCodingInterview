from linkedlist import LinkedList


def addLists(l1, l2, carry):
    if l1 == None and l2 == None and carry == 0:
        return None

    result = LinkedList(0)

    value = carry
    if l1 is not None:
        value += l1.val
    if l2 is not None:
        value += l2.val

    result.val = value % 10

    if l1 is not None or l2 is not None:
        more = addLists(l1.next if l1.next is not None else None, l2.next if l2.next is not None else None, 1 if value >= 10 else 0)
        result.next = more

    return result


def main():
    n1 = LinkedList(7)
    n2 = LinkedList(1)
    n3 = LinkedList(6)
    n4 = LinkedList(5)
    n5 = LinkedList(9)
    n6 = LinkedList(2)
    n1.next = n2
    n2.next = n3
    n4.next = n5
    n5.next = n6
    printLList(n1)
    printLList(n4)
    ll = addLists(n1, n4, 0)
    printLList(ll)


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
