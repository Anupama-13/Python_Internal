class Node:
    def __init__(self,data):
        self.data=data
        self.ls=None
        self.rs=None
class BinaryST:
    def insert(self,r,ele):
        n=Node(ele)
        if r==None:
            r=n
        else:
            prev=None
            t=r
            while t!=None:
                if t.data>ele:
                    prev=t
                    t=t.ls
                elif t.data<ele:
                    prev=t
                    t=t.rs
            if prev.data>ele:
                prev.ls=n
            else :
                prev.rs=n
        return r
    def Rsearch(self,r,key):
        if r is None:
            return
        if r.data==key:
            return r
        elif r.data>key:
            return self.Rsearch(r.ls,key)
        else:
            return self.Rsearch(r.rs,key)
    def NRsearch(self,r,key):
        if r is None:
            return 
        t=r
        while t!=None:
            if t.data==key:
                return t
            elif t.data>key:
                t=t.ls
            else:
                t=t.rs
        return t
r=None
bt=BinaryST()
n=int(input("ENter number of elements"))
for i in range(n):
    ele=int(input("ENter ele"))
    r=bt.insert(r, ele)
key=int(input("ENter key"))
c=int(input("ENter 1 for Recursive..... 2 for Non Recursive !"))
if(c==1):
    res_1=bt.Rsearch(r,key)
    if res_1 is None:
        print("Key not found")
    else:
        print("Key found...")
elif(c==2):
    res_1=bt.NRsearch(r,key)
    if res_1 is None:
        print("Key not found")
    else:
        print("Key found...")
else:
    print("Wrong choice")
