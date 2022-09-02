class DequeList:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l) ==0:
            return True
        else:
            return False
    def enqueLast(self,ele):
        self.l.append(ele)
    def enqueFirst(self,ele):
        self.l.insert(0,ele)
    def dequeFirst(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.l.pop(0)
    def dequeLast(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.l.pop(-1)
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are",self.l)
q=DequeList()
l=[]
n=int(input("ENter no of elements"))
for i in range(n):
    ele=int(input("Enter the element"))
    q.enqueLast(ele)
q.display()
ele=int(input("Enter element to insert at first"))
q.enqueFirst(ele)
q.display()
print("Deleting elemnt at last")
q.dequeLast()
q.display()
print("Deleting element at first")
q.dequeFirst()
q.display()
