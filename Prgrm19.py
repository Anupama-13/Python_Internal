class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class QueueLL:
    def __init__(self):
        self.r=None
        self.f=None
    def isEmpty(self):
        if self.f is None:
            return True
        else:
            return False
    def enqueue(self,elem):
        t=Node(elem)
        if self.r is None:
            self.r=t
            self.f=t
        else:
            self.r.next=t
            self.r=t
    def dequeue(self):
        if self.f is None:
            print("List is empty")
            return -1
        else:
            c=self.f
            self.f=self.f.next
            print("Deleted Element",c.data)
            del c
    def display(self):
        c=self.f
        while c!=None:
            print(c.data)
            c=c.next
l1=QueueLL()
n=int(input("Enter element into Queue(enter -1 to stop"))
while n!=-1:
    l1.enqueue(n)
    n=int(input("Enter element into queue"))
print("The list is ")
l1.display()
print("Deleting element at front end")
l1.dequeue()
print ("after deletion")
l1.display()

             
