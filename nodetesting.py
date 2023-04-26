class Node:
    def __init__(self, item):
        self.item = item
        self.nextitem = None

e1 = Node('mon')
e2 = Node('tue')
e3 = Node('wed')

e1.nextitem = e3
e3.nextitem = e2

thisvalue = e1
while thisvalue:
        print(thisvalue.item)
        thisvalue = thisvalue.nextitem

