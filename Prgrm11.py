def Isort(l,n):
    for i in range(1,n):
        t=l[i]
        j=i-1
        f=False
        while j>=0 and not f:
            if t<l[j]:
                l[j+1]=l[j]
                l[j]=t
                j=j-1
            else:
                f=True
            l[j+1]=t
        
    
l=[]
n=int(input("Enter no of elements"))
for i in range(0,n):
    ele=int(input("Enter element"))
    l.append(ele)
Isort(l,n)
print("Sorted list",l)
