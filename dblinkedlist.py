class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.head = Node(17)
    second = Node(25)
    third = Node(30)
    fourth = Node(67)
    linkedlist.head.next = second
    second.prev = linkedlist.head
    second.next = third
    third.prev = second
    third.next = fourth
    while linkedlist.head is not None:
        print(linkedlist.head.item)
        linkedlist.head = linkedlist.head.next