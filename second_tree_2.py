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
        connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_connection(sec_tree,len(name),name)
            return
        connection_test(ftree.right, name)


def sec_tree_connection(sec_tree, length, username):
    if sec_tree is not None:
        sec_tree_connection(sec_tree.left, length, username)
        if sec_tree.data == length:
            #sec_tree.sec_data = username
            #print("Found",sec_tree.sec_data,"as", length)
            #sec_tree.sec_data.append(chr(sortChar(sec_tree.sec_data)))
            sec_tree.sec_data.append(username)
            sort_char(sec_tree.sec_data)
            #print(sec_tree.sec_data)
            return
        sec_tree_connection(sec_tree.right, length, username)


def sec_connect(s_tree,length, search):
    if s_tree is not None:
        sec_connect(s_tree.left, length, search)
        if s_tree.data == length:
            print(s_tree.sec_data)
            result = binary_search(s_tree.sec_data, search)
            print(result)
            return
        sec_connect(s_tree.right, length, search)


def sort_char(sec_data: list):
    n = len(sec_data)
    for i in range(n-1):
        for j in range(n-1-i):
            if ascii_code(sec_data[j]) > ascii_code(sec_data[j+1]):
                temp = sec_data[j]
                sec_data[j] = sec_data[j+1]
                sec_data[j+1] = temp
    return sec_data


def ascii_code(char):
    totality = 0
    for element in char:
        totality += ord(element)
    return totality


def binary_search(s_tree: list, search):
    l = 0
    r = len(s_tree)-1
    while l <= r:
        mid=(l+r)//2
        if s_tree[mid] == search:
            return mid
        elif search < s_tree[mid]:
            r = mid-1
        elif search > s_tree[mid]:
            l = mid+1
    return -1


def email_cutting(mail):
    array = []
    f_mail = ''
    for i in mail:
        array += i
    for i in range(len(array)-10):
        f_mail += array[i]
    return f_mail

fst_tree = search_main.tree
sec_tree = second_tree.tree

if __name__ == '__main__':
    t = True
    while t:
        mail = input("Enter your e-mail:")
        name = email_cutting(mail)
        connection_test(fst_tree, name)
        ext = input("Enter \"e\" to exit \"or\" any key to continue: ")
        if ext == 'e':
            t = False
    s_mail = input("Enter search mail")
    search = email_cutting(s_mail)
    sec_connect(sec_tree,len(search), search)



