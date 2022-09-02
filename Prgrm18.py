class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class StackLL:
    def __init__(self):
        self.l=None
    def push(self,elem):
        t=Node(elem)
        if self.l is None:
            self.l=t
        else:
            t.next=self.l
            self.l=t
    def pop(self):
        if self.l is None:
            print("List is empty")
            return -1
        else:
            c=self.l
            self.l=self.l.next
            print("Deleted Element",c.data)
            del c
    def peek(self):
        if self.l is None:
            print("List is empty")
            return -1
        else:
            c=self.l
            print("Element at top is",c.data)
    def display(self):
        c=self.l
        while c!=None:
            print(c.data,"-->")
            c=c.next
l1=StackLL()
n=int(input("Enter element into LL,(enter -1 to stop)"))
while n != -1:
    l1.push(n)
    n=int(input("Enter elemnet"))
print("The list is ")
l1.display()
l1.peek()
print("Deleting top element")
l1.pop()
print ("after deletion")
l1.display()

             
