from linkedlist import LinkedList


def printKthToLast(head, k):
    if head is None:
        return 0
    index = printKthToLast(head.next, k) + 1
    if index == k:
        print(f'{k}th to last node is {head.val}')
    return index


def main():
    n1 = LinkedList(3)
    n2 = LinkedList(5)
    n3 = LinkedList(8)
    n4 = LinkedList(12)
    n5 = LinkedList(8)
    n6 = LinkedList(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    printLList(n1)
    printKthToLast(n1, 3)


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
