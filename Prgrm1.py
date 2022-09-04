details = []
N = int(input(" enter the range of list..\n"))
for i in range(N):
    l=[]
    l.append(input("enter the name  \n"))
    l.append(int(input("enter the age \n")))
    details.append(l)
print("The list of names nad ages before sorting is")
print(details)
print("The list after sorting based on age is")
print(sorted(details,key=lambda x:x[-1]))
