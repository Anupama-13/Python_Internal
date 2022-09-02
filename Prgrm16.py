class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class Deqsll:
    def __init__(self):
        self.r=None
        self.f=None
    def isEmpty(self):
        if self.f is None:
            return True
        else:
            return False
    def enqueFirst(self,ele):
        t=Node(ele)
        if self.f is None:
            self.f=t
            self.r=t
        else:
            t.next=self.f
            self.f=t
    def enqueLast(self,elem):
        t=Node(elem)
        if self.r is None:
            self.r=t
            self.f=t
        else:
            self.r.next=t
            self.r=t
    def dequeFirst(self):
        if self.f is None:
            print("List is empty")
            return -1
        else:
            c=self.f
            self.f=self.f.next
            print("Deleted Element",c.data)
            del c
    def dequeLast(self):
        if self.f is None:
            print("Dequeue is empty")
            return -1
        else:
            t=self.f
            if self.f==self.r:
                print("Deleted element is",t.data)
                del t
            else:
                while t.next!=None:
                    k=t
                    t=t.next
                print("deletd element is",t.data)
                self.r=k
                self.r.next=None
                del t
    def display(self):
        c=self.f
        while c!=None:
            print(c.data)
            c=c.next
d=Deqsll()
n=int(input("Enter element into Queue(enter -1 to stop"))
while n!=-1:
    d.enqueLast(n)
    n=int(input("Enter element into queue"))
print("The list is ")
d.display()
n=int(input("Enter an elemnet to insert at first"))
d.enqueFirst(n)
d.display()
print("Deleting element at front end")
d.dequeFirst()
d.display()
print("Deleting element at rear end")
d.dequeLast()
print ("after deletion")
d.display()

             
