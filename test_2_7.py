from linkedlist import LinkedList


def find_intersection(l1, l2):
    if l1 is None or l2 is None:
        return False

    r1 = get_tail_and_size(l1)
    r2 = get_tail_and_size(l2)

    if r1.tail is not r2.tail:
        return False

    shorter = l1 if r1.size < r2.size else l2
    longer = l2 if r1.size < r2.size else l1

    longer = get_kth_node(longer, abs(r1.size - r2.size))

    while (shorter != longer):
        shorter = shorter.next
        longer = longer.next

    return longer


class Result:
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size


def get_tail_and_size(n):
    if n is None:
        return None
    size = 0
    while (n.next is not None):
        size += 1
        n = n.next

    return Result(n, size)


def get_kth_node(head, k):
    current = head
    while (k > 0 and current is not None):
        current = current.next
        k -= 1
    return current


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

    n7 = LinkedList(1)
    n8 = LinkedList(2)
    n9 = LinkedList(1)
    n10 = LinkedList(2)
    n7.next = n8
    n8.next = n9
    n9.next = n10
    print(find_intersection(n1, n7))


def printLList(n):
    while n is not None:
        print(n.val)
        n = n.next


if __name__ == "__main__":
    main()
