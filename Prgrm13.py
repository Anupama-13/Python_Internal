def Ssort(l,n):
    for i in range(n-1):
        mi=i
        me=l[i]
        for j in range(i+1,n):
            if me>l[j]:
                me=l[j]
                mi=j
        if i!=mi:
            """l[mi]=l[i]
            l[i]=me"""
            t=l[i]
            l[i]=l[mi]
            l[mi]=t
l=[]
n=int(input("Enter no of elements"))
for i in range(0,n):
    ele=int(input("Enter element"))
    l.append(ele)
Ssort(l,n)
print("Sorted list",l)
