def Bsort(l,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if l[j]>l[j+1]:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
l=[]
n=int(input("Enter no of elements"))
for i in range(0,n):
    ele=input("Enter element")
    l.append(ele)
Bsort(l,n)
print("Sorted list",l)
