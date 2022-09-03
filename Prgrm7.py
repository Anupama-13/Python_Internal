def ip(sym):
    values={'+':1,'-':1,'*':3,'/':3,'^':6,'(':9,')':0}
    if sym in values.keys():
        return values[sym]
    else:
        return 7
def sp(sym):
    values={'+':2,'-':2,'*':4,'/':4,'^':5,'(':0,')':0}
    if sym in values.keys():
        return values[sym]
    else:
        return 8
class Stack:
    top=-1
    l=[]
    def isEmpty(self):
        if len(self.l) ==0:
            return True
        else:
            return False
    def push(self,ele):
        self.l.append(ele)
        self.top+=1
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            ele=self.l[self.top]
            self.l.pop()
            self.top-=1
            return ele
infix=input("Enter infix expression (exclude beginning brace ang include $ at end): ")
postfix=" "
s=Stack();
s.push('(')
for sym in infix:
    if sym=='$':
        break
    while(ip(sym)<sp(s.l[s.top])):
        postfix=postfix + s.pop()
    if(ip(sym)>sp(s.l[s.top])):
        s.push(sym)
    else:
        s.pop()
print("The postfix expression is")
print(postfix)
            
    
        
        

    
