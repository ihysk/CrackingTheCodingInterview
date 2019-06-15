from linkedlist import LinkedList


def deleteNode(n):
    if n is None or n.next is None:
        return False
    n_next = n.next
    n.val = n_next.val
    n.next = n_next.next
    return True


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
    deleteNode(n3)
    printLList(n1)


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
