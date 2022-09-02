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
            for i in self.l[::-1]:
                print(i,end=" ")
s=Stack()
n=int(input("enter number of chars in your stirng"))
for i in range(n):
    ele=input("Enter the string")
    s.push(ele)
s.display()
