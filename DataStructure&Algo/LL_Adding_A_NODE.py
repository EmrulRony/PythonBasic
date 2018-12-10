class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,newNode):
        myNode=Node(newNode)

        if (self.head==None):
            self.head=myNode

        lastNode=self.head
        while(lastNode.next!=None):
            lastNode=lastNode.next

        lastNode.next=myNode

llist = LinkedList()

llist.append(5)