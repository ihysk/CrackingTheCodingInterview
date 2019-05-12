from linkedlist import LinkedList


def nthToLast(head, k):
    p1 = head
    p2 = head

    for i in range(k):
        if p1.next is None:
            print('Out of range')
            return
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2

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
    tmp = nthToLast(n1, 12)
    print(tmp.val)


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
