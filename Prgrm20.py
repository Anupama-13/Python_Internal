class Stack:
    def __init__(self):
        self.l=[]
    def isEmpty(self):
        if len(self.l) ==0:
            return True
        else:
            return False
    def push(self,ele):
        self.l.append(ele)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.l.pop()
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.l[-1]
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements are",self.l)
s=Stack()
l=[]
n=int(input("ENter no of elements"))
for i in range(n):
    ele=int(input("Enter the element"))
    s.push(ele)
s.display()
print("Element at top is",s.peek())
print("Deleting element at top")
s.pop()
print("After deletion")
s.display()
