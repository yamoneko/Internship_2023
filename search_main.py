class Node:
    def __init__(self,data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


main_tree_data = []
for i in range(97,123):
    main_tree_data.append(chr(i))


def insert(root_tree: Node, alpha):
    if root_tree is None:
        return Node(alpha)
    if ord(alpha) < ord(root_tree.data):
        root_tree.left = insert(root_tree.left,alpha)
    else:
        root_tree.right = insert(root_tree.right,alpha)
    return root_tree


def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)


length = len(main_tree_data)
mid = int(length/2)
tree = Node('m')
#print(tree)

first_part = main_tree_data[0:mid-1]
second_part = main_tree_data[mid: length]

first_part.reverse()
for i in range(len(first_part)):
    tree = insert(tree, first_part[i])

for i in range(len(second_part)):
    tree = insert(tree, second_part[i])

#printing(tree)
