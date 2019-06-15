from linkedlist import LinkedList


def isPalindrome(head):
    reversed = reverseAndClone(head)
    return isEqual(head, reversed)


def reverseAndClone(node):
    head = None
    while (node is not None):
        n = LinkedList(node.val)
        n.next = head
        head = n
        node = node.next
    return head


def isEqual(l1, l2):
    while (l1 is not None and l2 is not None):
        if (l1.val != l2.val):
            return False
        l1 = l1.next
        l2 = l2.next
    return (l1 == None and l2 == None)


def main():
    n1 = LinkedList(3)
    n2 = LinkedList(5)
    n3 = LinkedList(8)
    n4 = LinkedList(12)
    n5 = LinkedList(7)
    n6 = LinkedList(5)
    n7 = LinkedList(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    printLList(n1)
    print(isPalindrome(n1))


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
