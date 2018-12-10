class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

# Adding a data at the start of the list
    def push(self,newData):
        objNode = Node(newData)
        objNode.next=self.head
        self.head=objNode

# Adding a node after a given node
llist = LinkedList()

llist.head=Node(5)
second =Node(4)
third =Node(5)

llist.head.next=second
second.next=third

llist.push(100)
