class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # def printItem(self):
    #     result = self.head
    #     while result is not None:
    #         print(result.item)
    #         result = result.next

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.head = Node(17)
    second = Node(25)
    third = Node(30)
    linkedlist.head.next = second
    second.next = third
    while linkedlist.head is not None:
        print(linkedlist.head.item)
        linkedlist.head = linkedlist.head.next