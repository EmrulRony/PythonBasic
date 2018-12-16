class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(Node):
    def __init__(self):
        self.head = None

    def add(self,newData):

        newNode = Node(newData)

        if (self.head==None):
            self.head=newNode

    # Adding a data at the start of the list

    def push(self, newData):
        objNode = Node(newData)
        objNode.next = self.head
        self.head = objNode

        # Adding a node after a given node

    def addafter(self, prev, newData):
        newNode = Node(newData)

        if (prev == None):
            print("The previous node should be in the linked list")

        newNode.next = prev.next
        prev.next = newNode

        # Adding a node at the end of the list

    def add(self,newData):
        newNode= Node(newData)


        if (self.head==None):
            self.head=newNode
            return

        last = self.head

        while (last.next!=None):
            last=last.next

        last.next=newNode

        # Delete a node by given value of the node

    def deleteNodeByKey(self,key):

        temp = self.head

        if (temp!=None):
            if (temp.data==key):
                self.head=temp.next
                temp==None
                return

        while (temp):
            if (temp.data==key):
                break

            prev = temp
            temp=temp.next

        if (temp==None):
            print("The data is not in the liked list")
            return


        prev.next=temp.next
        temp=None

        #Delete a node by given index num

    def delByIndex(self,indexNumber):

        if (self.head==None):
            return
        temp = self.head

        if (indexNumber==0):
            self.head = temp.next
            temp = None
            return


        # Find the previous number of the number we want to delete
        for i in range (0,indexNumber-1):
            temp=temp.next
            if (temp==None):
                break
        # If index number is more than the length of the list
        if temp==None:
            return
        if temp.next==None:
            return
        next = temp.next.next

        temp.next=None

        temp.next=next

    # Print the linked list
    def print(self):

        temp=self.head

        if (self.head==None):
            print("The list is empty")
            return

        while(temp.next):
            print(temp.data, end=" ")
            temp=temp.next
        print(temp.data, end=" ")
    # Count the indexes of node

    def count(self):

        count = 0
        temp = self.head
        while(temp!=None):
            temp=temp.next
            count=count+1

        print(count)

    def search(self,searchData):

        temp = self.head
        if (temp==None):
            return
        while(temp!=None):
            if (temp.data==searchData):
                return True
            temp=temp.next
        return False

class main():

    llist = LinkedList()
    llist.add(6)
    llist.add(7)
    llist.add(8)
    llist.add(10)

    llist.addafter(llist.head.next.next.next,'X')
    print('Before deleting list')
    llist.print()
    print()
    print('after deleting list')
    # llist.deleteNodeByKey(10)
    # llist.delByIndex(2)
    llist.print()
    print()
    llist.count()
    print(llist.search(10))

main()

