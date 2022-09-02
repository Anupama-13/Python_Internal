class Node:
    def __init__(self,elem):
        self.data=elem
        self.next=None
class LinkedList:
    def __init__(self):
        self.l=None

    def create(self):
        ele=int(input("Enter elements into SLL(enter -1 to stop)"))
        while ele!=-1:
            t=Node(ele)
            if self.l is None:
                self.l=t
                p=t
            else:
                p.next=t
                p=t
            ele=int(input("Enter elemnet"))
    def delete(self,value):
        if self.l is None:
            print("List is empty")
            return -1
        else:
            if self.l.data==value:
                t=self.l
                self.l=self.l.next
                del t
            else:
                c=self.l
                p=None
                while c!=None and value!=c.data:
                    p=c
                    c=c.next
                if c==None:
                    print("Element is not there")
                    return -1
                else:
                    p.next=c.next
                    del c
    def display(self):
        c=self.l
        while c!=None:
            print(c.data,end="-->")
            c=c.next
l1=LinkedList()
l1.create()
print("The list is ")
l1.display()
d1=int(input("Enter elem to delete"))
l1.delete(d1)
print("After deletion ")
l1.display()

             
