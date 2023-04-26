s_tree = [1,2,3,4,5,6,7]
search = 4


def binary_search(s_tree: list, search):
    l=0
    r=len(s_tree)-1
    while l <= r:
        mid=(l+r)//2
        if s_tree[mid] == search:
            return mid
        elif search < s_tree[mid]:
            r = mid-1
        elif search > s_tree[mid]:
            l = mid+1
    return -1


#print(binary_search(s_tree,search))


mail = 'ya@gmail.com'


def email_cutting(mail):
    array = []
    f_mail = ''
    for i in mail:
        array += i
    for i in range(len(array)-10):
        f_mail += array[i]
    return f_mail


print(email_cutting(mail))


# def ascii_code(char):
#     totality = 0
#     for element in char:
#         totality += ord(element)
#     return totality
# #
# # print(ascii_code('dda'))
#
#
# sec_data = ['m', 'b', 'k', 'a']


# def sort_char(sec_data):
#     n = len(sec_data)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if ascii_code(sec_data[j]) > ascii_code(sec_data[j+1]):
#                 temp = sec_data[j]
#                 sec_data[j] = sec_data[j+1]
#                 sec_data[j+1] = temp
#     return sec_data
#
#
# print(sort_char(sec_data))
