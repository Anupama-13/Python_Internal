def nrbinary(a,key):
    lb=0
    ub=len(l)-1
    while lb<=ub:
        mid=(lb+ub)//2
        if key ==a[mid]:
            return mid
        elif key<a[mid]:
            ub=mid-1
        else:
            lb=mid+1
    return -1
l=[]
n=int(input("enter number of elements"))
for i in range(n):
    ele=int(input("enter the element"))
    l.append(ele)
l.sort()
key=int(input("enter element to search"))
idx=nrbinary(l,key)
if idx is -1:
    print("Element is not found")
else:
    print("Element found at ",idx," location")

