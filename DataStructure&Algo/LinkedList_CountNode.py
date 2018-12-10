class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList():
    def __init__(self):
        self.head=None

class CountList(Node):
    def __init__(self,head):
        Node.__init__(self,data=None)
        self.lhead=head

    def count(self):
        count = 1
        first=self.lhead
        while(first.next!=None):
            first=first.next
            count=count+1
        return count

llist = LinkList()

llist.head=Node(5)
second= Node(3)
third = Node(4)
fourth= Node (7)
fifth= Node(11)

llist.head.next=second
second.next=third
third.next=fourth
fourth.next=fifth

count = CountList(llist.head)
print(count.count())
