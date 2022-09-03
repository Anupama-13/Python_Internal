def isOperator(i):
    operator=['+','-','*','/','^']
    if i in operator:
        return True
    else:
        return False
def evaluation(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    elif op=='^':
        return b**a
    else:
        print("Invalid operator")
        return
postfix=input("Enter postfix expression")
temp=[]
for i in postfix:
    if isOperator(i):
        v1=int(temp.pop())
        v2=int(temp.pop())
        ans=evaluation(v1,v2,i)
        temp.append(ans)
    else:
        temp.append(i)
print("The postfix expression result is")
print(temp[0])
