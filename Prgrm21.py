class Queue:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l) ==0:
            return True
        else:
            return False
    def enque(self,ele):
        self.l.append(ele)
    def deque(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.l.pop(0)
    def front(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.l[0]
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are",self.l)
q=Queue()
l=[]
n=int(input("ENter no of elements"))
for i in range(n):
    ele=int(input("Enter the element"))
    q.enque(ele)
q.display()
print("Element at front is",q.front())
print("Deleting element at top")
q.deque()
print("After deletion")
q.display()
