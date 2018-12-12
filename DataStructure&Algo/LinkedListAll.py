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
    def insertAfter(self,prevNode,newData):
        newNode = Node(newData)

        if (prevNode==None):
            print("Privious node must be in the link list")
            return
        newNode.next=prevNode.next
        prevNode.next=newNode

#Adding a node at the end of the linked list

    def append(self,newData):

        newNode=Node(newData)

        if self.head is None:
            self.head=newNode
        last=self.head
        while(last.next):
            last=last.next

        last.next=newNode
# Printing the Linked list

    def printList(self):
        temp=self.head
        while(temp):
            print (temp.data)
            temp=temp.next


llist = LinkedList()

llist.head=Node(5)
second =Node(4)
third =Node(5)

llist.head.next=second
second.next=third
llist.append(500)
llist.printList()
