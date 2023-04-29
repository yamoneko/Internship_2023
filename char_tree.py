class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


if __name__ == '__main__':
    root_tree = Node('m')
    main_tree_data = []
    for i in range(97, 123):
        main_tree_data.append(chr(i))
    for i in range(len(main_tree_data)):
        root_tree.insert(main_tree_data[i])
    root_tree.print_tree()

