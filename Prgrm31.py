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
    def preorder(self,r):
        if r is None:
            return
        print(r.data,end=" ")
        self.preorder(r.ls)
        self.preorder(r.rs)
    def inorder(self,r):
        if r is None:
            return
        self.inorder(r.ls)
        print(r.data,end=" ")
        self.inorder(r.rs)
    def postorder(self,r):
        if r is None:
            return
        self.postorder(r.ls)
        self.postorder(r.rs)
        print(r.data,end=" ")
r=None
bt=BinaryST()
n=int(input("ENter number of elements"))
for i in range(n):
    ele=int(input("ENter ele"))
    r=bt.insert(r, ele)
print("The preorder traversal of BST is")
bt.preorder(r)
print("\nThe Inorder traversal of BST is")
bt.inorder(r)
print("\nThe postorder traversal of BST is")
bt.postorder(r)


