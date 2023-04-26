import search_main
import second_tree

fst_tree = search_main.tree
sec_tree = second_tree.tree


class ThirdThree:
    def __init__(self,data):
        self.data = data
        self.same_length: list = [] #tree length nae thu tae data ko thi mhr lar save
        self.left = None
        self.right = None


def printing(node):
    if node is not None:
        printing(node.left)
        if node.sec_data is not None:
            print(node.sec_data)
        printing(node.right)


def connection_test(ftree, name):
    if ftree is not None:
        #connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_connection(sec_tree,len(name),name)
            return
        #connection_test(ftree.right, name)


def sec_tree_connection(sec_tree, length, name):
    if sec_tree is not None:
        sec_tree_connection(sec_tree.left, length, name)
        if sec_tree.data == length:
            sec_tree.sec_data = name
            print("We found", sec_tree.sec_data, "at", length)
            third_tree_connection(trd_tree,length,name)
            return
        sec_tree_connection(sec_tree.right, length, name)


def third_tree_connection(third_tree ,length, name):
    if third_tree is not None:
        if third_tree.data == length:
            third_tree.same_length.append(name)
        print("Same length data", third_tree.same_length)


#def insertIntoThirdTree(third_tree: ThirdThree, data)

trd_tree = ThirdThree(5)
if __name__ == '__main__':
    while True:
        name = input("Enter name:")
        connection_test(fst_tree, name)





