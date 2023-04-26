class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def AtNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def printlinkedlist(self):
        result = self.head
        while result is not None:
            print(result.item)
            result = result.next


def getData():
    user = {}
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    birthday = input("Enter your birthday: ")
    budget = input("Enter your budget point")
    user.update({"name": name, "email": email, "password": password, "birthday": birthday, "budget": budget})
    return user


if __name__ == '__main__':
    linkedlist = Linkedlist()
    for i in range(5):
        userdata = getData()

        if linkedlist.head is None:
            linkedlist.head = Node(userdata)


        else:
            res = linkedlist.head
            while res is not None:
                if res.item["email"] == userdata["email"]:
                    print("Your email is not unique..please try again::::")
                    break
                res = res.next

            else:
                linkedlist.AtNode(userdata)
    linkedlist.printlinkedlist()
