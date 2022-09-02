def rbinary(a,key,lb,ub):
    while lb<ub:
        mid=(lb+ub)//2
        if key ==a[mid]:
            return mid
        elif key<a[mid]:
            return rbinary(a,key,lb,mid-1)
        else:
            return rbinary(a,key,mid+1,ub)
    return -1
l=[]
n=int(input("enter number of elements"))
for i in range(n):
    ele=int(input("enter the element"))
    l.append(ele)
l.sort()
key=int(input("enter element to search"))
idx=rbinary(l,key,0,n-1)
if idx is -1:
    print("Element is not found")
else:
    print("Element found at ",idx," location")
    
