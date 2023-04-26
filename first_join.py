import search_main
import second_tree


def printing(node):
    if node is not None:
        printing(node.left)
        if node.sec_data is not None:
            print(node.sec_data)
        printing(node.right)


# def printed(node):
#     if node is not None:
#         printing(node.left)
#         print(node.data)
#         printing(node.right)


def connection_test(ftree, name):
    if ftree is not None:
        #connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_connection(sec_tree,len(name),name)
            return
        #connection_test(ftree.right, name)


def sec_tree_connection(sec_tree, length, username):
    if sec_tree is not None:
        sec_tree_connection(sec_tree.left, length, username)
        if sec_tree.data == length:
            sec_tree.sec_data = username
            print("Found",sec_tree.sec_data,"as", length)
            return
        sec_tree_connection(sec_tree.right, length, username)


fst_tree = search_main.tree
sec_tree = second_tree.tree

if __name__ == '__main__':
    while True:
        name = input("Enter name:")
        connection_test(fst_tree, name)
