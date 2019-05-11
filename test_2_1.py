from linkedlist import LinkedList


def deleteDups(n):
    s = set()
    previous = LinkedList(None)
    while(n is not None):
        if n.val in s:
            previous.next = n.next
        else:
            s.add(n.val)
            previous = n
        n = n.next


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
    deleteDups(n1)
    printLList(n1)


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
