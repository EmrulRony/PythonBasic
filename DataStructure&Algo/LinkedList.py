class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkList:
    def __init__(self):
        self.head=None


    def countNode(self,head):
        count=1
        current=self.head
        while(current.next!=None): #second.next jodi null na hoy
                current=current.next
                count=count+1
        return count


llist = LinkList()
llist.head=Node(5)
second = Node(4)
third = Node(11)
four=Node(12)

llist.head.next=second #>4
second.next=third #>11
third.next=four

print(llist.countNode(llist.head))
print(llist.printList(second))



